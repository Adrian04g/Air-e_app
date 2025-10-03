from django.contrib import admin
from django.contrib.auth.models import User
from .models import Cableoperadores

admin.site.register(Cableoperadores)
# Unregister the User model from the admin site
admin.site.unregister(User)
# Admin 
from django.contrib.auth.admin import UserAdmin
@admin.register(User)
class NewAdmin(UserAdmin):
    pass