from django.contrib import admin
from django.contrib.auth.models import User
from .models import Cableoperadores, Cable, Caja_empalme, Contratos, Nap, Usos, Reserva

admin.site.register(Cableoperadores)
admin.site.register(Cable)
admin.site.register(Caja_empalme)
admin.site.register(Contratos)
admin.site.register(Nap)
admin.site.register(Usos)
admin.site.register(Reserva)
# Unregister the User model from the admin site
admin.site.unregister(User)
# Admin 
from django.contrib.auth.admin import UserAdmin
@admin.register(User)
class NewAdmin(UserAdmin):
    pass