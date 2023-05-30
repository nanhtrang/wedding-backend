from django.contrib import admin
from .models import Wish, Confirm, Account

# Register your models here.
admin.site.register(Wish)
admin.site.register(Confirm)
admin.site.register(Account)