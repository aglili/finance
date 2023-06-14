from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .serializer import ExpenseSerializer,BudgetSerializer
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Expenses,Budget,get_budget_remaining
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



@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def getUserExpensesByMonth(request):
    user = request.user
    month = request.GET.get('month')
    year = request.GET.get('year')

    expenses = Expenses.objects.filter(user=user,date__month=month,date__year=year)
    serializer = ExpenseSerializer(expenses,many=True)
    return Response({"data":serializer.data},status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def CreateBudget(request):
    serializer = BudgetSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Budget Created","data":serializer.data},status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def getRemainingBudgetAmount(request):
    user = request.user
    category = request.GET.get('category')
    try:
        remaining_budget = get_budget_remaining(user=user,category=category)
        return Response({"remaining_amount": remaining_budget}, status=status.HTTP_200_OK)
    except Budget.DoesNotExist:
        return Response({"error": "Budget not found"}, status=status.HTTP_404_NOT_FOUND)
