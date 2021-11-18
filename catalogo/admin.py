from django.contrib import admin
from .models import Libro, Autor, Direccion, Pais
# Register your models here.

class LibroAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {'slug': ('titulo',)}
    list_filter = ("es_bestseller", 'puntaje')
    list_display = ("titulo", "autor",)

admin.site.register(Libro, LibroAdmin)
admin.site.register(Autor)
admin.site.register(Direccion)
admin.site.register(Pais)