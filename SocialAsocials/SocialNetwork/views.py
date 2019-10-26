from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Post, Comment
from .serializers import UserSerializer


# Create your views here.
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET', "POST"])
class ProfileView(viewsets.ModelViewSet):
    def get(self, username):
        queryset = User.objects.filter(username=username).one()
        serializer_classz= UserSerializer
