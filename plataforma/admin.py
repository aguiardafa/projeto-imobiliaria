from django.contrib import admin

from .models import DiaVisita, Horario, Imovel, Cidade, Imagem, Visita


# Register your models here.
@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo_imovel', 'rua', 'valor', 'quartos', 'tamanho', 'cidade', 'tipo')
    list_editable = ('valor', 'tipo')
    list_filter = ('cidade', 'tipo')


@admin.register(Visita)
class VisitaAdmin(admin.ModelAdmin):
    list_display = ('id', 'imovel', 'usuario', 'dia', 'horario', 'status')
    list_editable = ('status',)
    list_filter = ('imovel', 'usuario', 'dia', 'status')


admin.site.register(DiaVisita)
admin.site.register(Horario)
admin.site.register(Imagem)
admin.site.register(Cidade)
