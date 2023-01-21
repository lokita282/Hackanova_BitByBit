from django.shortcuts import render
from django.http import HttpResponse, FileResponse
import webbrowser
from apis.views import report
# Create your views here.

def onlineMeet(request):
    link = "https://console.agora.io/invite?sign=0535b61d1e6d22ab32e27bd16b1f181e%253A4db31330d68186d59fb2868a1b09b4589b7d13be79eb0e425ad4c4313cb699e0"
    webbrowser.open(link, 2)
    img = open('report_temp.jpg', 'rb')

    response = FileResponse(img)

    return response