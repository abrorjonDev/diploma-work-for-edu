from django.urls import path

from users.views import UserRegisterAPIView


urlpatterns = [
   path('sign-up/', UserRegisterAPIView.as_view(), name='register')
]