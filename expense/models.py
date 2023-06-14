from django.db import models
from accounts.models import CustomUser

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

    


    def __str__(self) -> str:
        return f"{self.user.get_full_name()} {self.date}"
    

    
