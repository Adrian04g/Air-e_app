from django.contrib import admin
from .models import Cable, Caja_empalme, Contratos, Nap, Reserva
# Register your models here.
admin.site.register(Cable)
admin.site.register(Caja_empalme)
admin.site.register(Contratos)
admin.site.register(Nap)
admin.site.register(Reserva)
