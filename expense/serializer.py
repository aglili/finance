from rest_framework import serializers
from . models import Expenses,Budget
from .emailsender import send_email_to_user



class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = ['id','user','amount', 'date', 'category', 'description']


    def create(self, validated_data):
        user = validated_data['user']
        amount = validated_data['amount']
        category = validated_data['category']
        date = validated_data['date']
        
        try:
            budget = Budget.objects.get(user=user, category=category)
            if amount > budget.limit:
                message = f"Dear {user.username}, The amount for the expense is above the budget limit"
                send_email_to_user(email=user.email, subject="Amount Exceeds Budget Limit", message=message)
            else:
                budget.limit -= amount
                budget.save()
        except Budget.DoesNotExist:
            pass
        
        expense = Expenses.objects.create(user=user, amount=amount, category=category, description=validated_data['description'],date=validated_data['date'])
        return expense

    



class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['user', 'category', 'limit', 'start_date', 'end_date']