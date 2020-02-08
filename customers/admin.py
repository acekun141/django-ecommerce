from django.contrib import admin
from customers.models import Customer, Bill

admin.site.register(Customer)
admin.site.register(Bill)