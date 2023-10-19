from django.contrib import admin

# Register your models here.
from .models import Usuario, Evento, Registrado

admin.site.register(Usuario)
admin.site.register(Evento)
admin.site.register(Registrado)