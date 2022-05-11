from django.contrib import admin
from .models import CustomUser


class AdminCustomUser(admin.ModelAdmin):
    pass


admin.site.register(CustomUser, AdminCustomUser)
