from django.contrib import admin
"""
Sistema de gestão para peritos
Autor: Fernando Torres Ferreira
https://fertorresfs.github.io/

comando para rodar

python .\manage.py runserver

acesso: 127.0.0.1:8000/admin
usuario: perito
senha: perito
forexsys
"""
# Register your models here.
from .models import Processos
from .models import Juiz
from .models import Auxiliar_justica
from .models import Vara

class ProcessosAdmin(admin.ModelAdmin):
    fields = ["id_processo",
             "id_juiz",
             "id_vara",
             "requerido",
             "requerente",
             "id_aux_jus",
             "honorarios",
             "data_nomeacao",
             "data_laudo_protocolado",
             "data_intimacao",
             "assunto",
             "data_inicio_pericia",
             "data_final_pericia",
             "data_aceite"]

#class JuizAdmin(admin.ModelAdmin):
#    fieldsets = [()]

class VaraAdmin(admin.ModelAdmin):
    fields = ["id_vara",
              "endereco",
              "tel",
              "email",
              "cidade",
              "estado",
              "nome"]

admin.site.register(Processos, ProcessosAdmin)
admin.site.register(Juiz)
admin.site.register(Auxiliar_justica)
admin.site.register(Vara, VaraAdmin)