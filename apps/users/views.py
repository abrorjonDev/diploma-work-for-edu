from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

from users.serializers import UserCreateSerializer


class UserRegisterAPIView(CreateAPIView):
    """Register new user."""
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = (AllowAny, )


