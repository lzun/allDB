from django.contrib import admin
from .models import Paciente
from .models import Medicos

# Register your models here.

#admin.site.register(Paciente)
admin.site.register(Medicos)

class CodeAdmin(admin.ModelAdmin):
	#fields = ['nombre', 'apellidos', 'medico']

	list_display = ('nombre', 'apellidos', 'medico')
	search_fields = ['nombre', 'apellidos', 'medico__nombre', 'medico__apellido']

admin.site.register(Paciente, CodeAdmin)
