import cv2
import numpy as np
import mediapipe as mp
import threading
import streamlit as st
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
from mediapipe.python.solutions.face_mesh_connections import FACEMESH_CONTOURS

# Create your views here.

@gzip.gzip_page 
def Home(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass
    return render(request, 'index.html')

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        frame = self.frame
        with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        
            blank_bg = cv2.imread("black background.jpg")
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = holistic.process(image)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            # 1. Draw face landmarks
            mp_drawing.draw_landmarks(blank_bg, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION, 
                                    mp_drawing.DrawingSpec(color=(120,110,10), thickness=1, circle_radius=1),
                                    mp_drawing.DrawingSpec(color=(120,256,121), thickness=1, circle_radius=1)
                                    )
            
            # 2. Draw Right hand landmarks
            mp_drawing.draw_landmarks(blank_bg, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                                    mp_drawing.DrawingSpec(color=(80,22,10), thickness=2, circle_radius=4),
                                    mp_drawing.DrawingSpec(color=(80,44,121), thickness=2, circle_radius=2)
                                    )

            # 3. Draw Left Hand landmarks
            mp_drawing.draw_landmarks(blank_bg, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                                    mp_drawing.DrawingSpec(color=(121,22,76), thickness=2, circle_radius=4),
                                    mp_drawing.DrawingSpec(color=(121,44,250), thickness=2, circle_radius=2)
                                    )

            # 4. Draw Pose Detections
            mp_drawing.draw_landmarks(blank_bg, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS, 
                                    mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=4),
                                    mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                                    )
        _, jpeg = cv2.imencode('.jpg', blank_bg)
        # return image
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()
            

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


#################################################### Sam 2


def gen_frame():
    while True:
        camera = cv2.VideoCapture(0)
        success, frame = camera.read()
        if not success:
            print(1)
            break
        
        else:
            mp_drawing = mp.solutions.drawing_utils
            mp_drawing_styles = mp.solutions.drawing_styles
            mp_holistic = mp.solutions.holistic

            with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
            
                blank_bg = cv2.imread("black background.jpg")
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = holistic.process(image)
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                
                # 1. Draw face landmarks
                mp_drawing.draw_landmarks(blank_bg, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION, 
                                        mp_drawing.DrawingSpec(color=(120,110,10), thickness=1, circle_radius=1),
                                        mp_drawing.DrawingSpec(color=(120,256,121), thickness=1, circle_radius=1)
                                        )
                
                # 2. Draw Right hand landmarks
                mp_drawing.draw_landmarks(blank_bg, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                                        mp_drawing.DrawingSpec(color=(80,22,10), thickness=2, circle_radius=4),
                                        mp_drawing.DrawingSpec(color=(80,44,121), thickness=2, circle_radius=2)
                                        )

                # 3. Draw Left Hand landmarks
                mp_drawing.draw_landmarks(blank_bg, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                                        mp_drawing.DrawingSpec(color=(121,22,76), thickness=2, circle_radius=4),
                                        mp_drawing.DrawingSpec(color=(121,44,250), thickness=2, circle_radius=2)
                                        )

                # 4. Draw Pose Detections
                mp_drawing.draw_landmarks(blank_bg, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS, 
                                        mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=4),
                                        mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                                        )
                                
                ret, buffer = cv2.imencode('.jpg', blank_bg)
                blank_bg = buffer.tobytes()
                yield (b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + blank_bg + b'\r\n')

def Home2():
    return render('index.html')

def video_feed(request):
    print(1)    
    return StreamingHttpResponse(gen_frame(), content_type="multipart/x-mixed-replace;boundary=frame")



















################################ Code fir Holistic 
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic

                
# def video_feed(request):
#     return StreamingHttpResponse(VR(), content_type='multipart/x-mixed-replace; boundary=frame')

def VR(request):
    cap = cv2.VideoCapture(0)
    # Initiate holistic model
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        
        while cap.isOpened():
            blank_bg = cv2.imread("black background.jpg")
            ret, frame = cap.read()
            
            # Convert the feed from BGR to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Refer the section above how to make detections on feed
            results = holistic.process(image)
    
            # Recolor image back to BGR for rendering
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            # 1. Draw face landmarks
            mp_drawing.draw_landmarks(blank_bg, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION, 
                                    mp_drawing.DrawingSpec(color=(120,110,10), thickness=1, circle_radius=1),
                                    mp_drawing.DrawingSpec(color=(120,256,121), thickness=1, circle_radius=1)
                                    )
            
            # 2. Draw Right hand landmarks
            mp_drawing.draw_landmarks(blank_bg, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                                    mp_drawing.DrawingSpec(color=(80,22,10), thickness=2, circle_radius=4),
                                    mp_drawing.DrawingSpec(color=(80,44,121), thickness=2, circle_radius=2)
                                    )

            # 3. Draw Left Hand landmarks
            mp_drawing.draw_landmarks(blank_bg, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                                    mp_drawing.DrawingSpec(color=(121,22,76), thickness=2, circle_radius=4),
                                    mp_drawing.DrawingSpec(color=(121,44,250), thickness=2, circle_radius=2)
                                    )

            # 4. Draw Pose Detections
            mp_drawing.draw_landmarks(blank_bg, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS, 
                                    mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=4),
                                    mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                                    )
                            
            cv2.imshow('Holistic Model Detections', blank_bg)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
            if cv2.waitKey(5) & 0xFF == 27:
                break

    cap.release()
    cv2.destroyAllWindows()

    return render(request, 'home.html')