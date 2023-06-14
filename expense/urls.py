from django.urls import path
from . import views



urlpatterns=[
    path("add/",views.createExpense,name="create_expense"),
    path("expenses/",views.getUserExpensesByMonth,name="get_expense_by_month"),
    path("expenses/all/",views.getUserExpenses,name="get_user_expenses")
]