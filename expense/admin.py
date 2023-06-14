from django.contrib import admin
from .models import Expenses,Budget

# Register your models here.
admin.site.register([Expenses,Budget])