from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializer import UserSignUpSerializer,UserLoginSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(["POST"])
def userSignUp(request):
    serializer = UserSignUpSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Sign Up Sucessful","data":serializer.data},status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
@api_view(["POST"])
def userLogin(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        response = serializer.get_jwt_token(data=request.data)
        return Response(response,status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
