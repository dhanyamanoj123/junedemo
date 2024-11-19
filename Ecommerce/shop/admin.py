from django.contrib import admin

# Register your models here.
from shop.models import Catergory
admin.site.register(Catergory)
from shop.models import Products
admin.site.register(Products)

from shop.models import User
admin.site.register(User)
