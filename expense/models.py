from django.db import models
from accounts.models import CustomUser
from .emailsender import send_email_to_user
from django.db.models import Sum


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




class Budget(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.CharField(max_length=200)
    limit = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.category} Budget"
    



def get_budget_remaining(user, category):
    budget = Budget.objects.get(user=user, category=category)
    total_expenses = Expenses.objects.filter(user=user, category=category).aggregate(Sum('amount'))['amount__sum']
    if total_expenses is None:
        total_expenses = 0
    remaining_amount = budget.limit - total_expenses
    return remaining_amount
    
