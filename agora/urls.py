from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='agora-index'),
    path('pusher/auth/', pusher_auth, name='agora-pusher-auth'),
    path('token/', generate_agora_token, name='agora-token'),
    path('call-user/', call_user, name='agora-call-user'),
]


