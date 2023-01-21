from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

import pywhatkit
from datetime import datetime


def send(request):
    currentDateAndTime = datetime.now()
    hour = currentDateAndTime.hour
    minute = currentDateAndTime.minute + 1
    doc_name = "Sarthak"
    number = '+918492010352'
    message = "Your meeting has been scheduled with Dr. " + doc_name + "on 23rd Jan, 2023 at 11:15am. Best Wishes :)"
    pywhatkit.sendwhatmsg_instantly(number, message)

    return redirect('http://localhost:3000')
