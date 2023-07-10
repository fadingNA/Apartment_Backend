from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from dorm_setup.dorm_setup.dormstart.serializers import UserSerializer, GroupSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API ENDPOINT HERE TO ALLOW USER
    EDIT THEIR INFORMATIONs
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
