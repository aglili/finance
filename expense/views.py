from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .serializer import ExpenseSerializer
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Expenses

# Create your views here.

@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def createExpense(request):
    serializer = ExpenseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"New Expense Created","data":serializer.data},status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def getUserExpenses(request):
    user = request.user
    expenses = Expenses.objects.filter(user=user)
    serializer = ExpenseSerializer(expenses,many=True)
    return Response({"data":serializer.data},status=status.HTTP_200_OK)