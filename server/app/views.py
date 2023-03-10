from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
# Create your views here.


@api_view(['GET'])
def getServer(request):
    return Response("Sever Initialized and Online. Ready to take OFF!", status=status.HTTP_200_OK)


@api_view(['GET', 'PUT'])
@permission_classes((IsAuthenticated))
def profile(request):
    user = request.user