from django.urls import path
from . import views



urlpatterns=[
    path("add/",views.createExpense,name="create_expense")
]