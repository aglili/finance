from rest_framework import serializers
from . models import Expenses,Budget



class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = ['id','user','amount', 'date', 'category', 'description']



class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['user', 'category', 'limit', 'start_date', 'end_date']