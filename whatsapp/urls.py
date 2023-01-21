from django.urls import path
from .views import *

urlpatterns = [
    path('', send, name = 'send'),
    path('sos/', sos, name='sos'),

]