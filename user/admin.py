from django.contrib import admin
from . models import Profile, Account, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(Account)