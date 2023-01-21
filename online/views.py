from django.shortcuts import render
from django.http import HttpResponse, FileResponse
import webbrowser
from apis.views import report
# Create your views here.

def onlineMeet(request):
    webbrowser.open('https://console.agora.io/invite?sign=eb5105ce6a6e624f99729809ff681f5d%253Aa83437bd5081355f0f7f62be39c752fedea69bda71561b91afdf2888ceb11f6f', 2)
    img = open('report_temp.jpg', 'rb')

    response = FileResponse(img)

    return response