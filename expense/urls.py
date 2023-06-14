from django.urls import path
from . import views



urlpatterns=[
    path("add/",views.createExpense,name="create_expense"),
    path("expenses/all/",views.getUserExpenses,name="get_user_expenses")
]