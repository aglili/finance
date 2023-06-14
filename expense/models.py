from django.db import models
from accounts.models import CustomUser
from .emailsender import send_email_to_user

# Create your models here.

class Expenses(models.Model):

    CATEGORY_CHOICES = [
    ('groceries', 'Groceries'),
    ('utilities', 'Utilities'),
    ('entertainment', 'Entertainment'),
    ('travel', 'Travel'),
    ('dining', 'Dining'),
    ('shopping', 'Shopping'),
    ('housing', 'Housing'),
    ('transportation', 'Transportation'),
    ('healthcare', 'Healthcare'),
    ('education', 'Education'),
    ('insurance', 'Insurance'),
    ('debt', 'Debt'),
    ('subscriptions', 'Subscriptions'),
    ('personal care', 'Personal Care'),
    ('gifts', 'Gifts'),
    ('charity', 'Charity'),
    ('savings', 'Savings'),
    ('investments', 'Investments'),
    ('other', 'Other'),
]

    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=200,choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=300)

    

    def __str__(self):
        return f"{self.user.username} - Expense"

    def create(self, validated_data):
        user = validated_data['user']
        amount = validated_data['amount']
        category = validated_data['category']

        try:
            budget = Budget.objects.get(user=user,category=category)
            if amount>budget.limit:
                message = f"Dear {self.user.username}, The Amount for the expense is above the budget limit"
                send_email_to_user(email=self.user.email,subject="Amount Exceeds Budget Limit",message=message)
            else:
                budget.limit -= amount
                budget.save()
        except Budget.DoesNotExist:
            pass
        expense = Expenses.objects.create(user=user, amount=amount, category=category, description=validated_data['description'])
        return expense


class Budget(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.CharField(max_length=200)
    limit = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.category} Budget"
    

    
