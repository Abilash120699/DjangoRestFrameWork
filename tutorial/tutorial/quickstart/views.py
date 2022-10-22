from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User,Group
from .serializers import UserSerializer,GroupSerializer
# Create your views here.


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission = [permissions.IsAuthenticated]

class GroupViewset(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission = [permissions.IsAuthenticated]
