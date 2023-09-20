from django.contrib import admin

from api.v1.accounts.models import CustomUser

# Register your models here.

admin.site.register(CustomUser)