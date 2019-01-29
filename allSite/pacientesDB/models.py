from django.db import models

# Create your models here.

class Medicos(models.Model):
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30)
	lugar_consulta = models.CharField(max_length=30, blank=True, null=True)

	def __str__(self):
		return self.nombre + ' ' + self.apellido

class Paciente(models.Model):
	SUBLINGUAL = 'SUBL'
	SUBCUTANEA = 'SUBC'
	TREATMENT_CHOICES = (
		(SUBLINGUAL, 'Sublingual'), 
		(SUBCUTANEA, 'Subcutaneo'),
	)

	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	medico = models.ForeignKey(Medicos, on_delete = models.CASCADE)
	formula = models.TextField()
	tratamiento = models.CharField(max_length=15,
		choices = TREATMENT_CHOICES,
		default = SUBLINGUAL,
		)
	volumen = models.IntegerField(blank=True, null=True)
	observaciones = models.TextField(blank=True, null=True)
	Frasco00 = models.DateField(blank=True, null=True)
	Frasco0 = models.DateField(blank=True, null=True)
	Frasco1 = models.DateField(blank=True, null=True)
	Frasco2 = models.DateField(blank=True, null=True)
	Frasco3 = models.DateField(blank=True, null=True)
	Frasco4 = models.DateField(blank=True, null=True)
	Frasco5 = models.DateField(blank=True, null=True)
	Frasco6 = models.DateField(blank=True, null=True)
	Frasco7 = models.DateField(blank=True, null=True)
	Frasco8 = models.DateField(blank=True, null=True)
	Frasco9 = models.DateField(blank=True, null=True)
	Frasco10 = models.DateField(blank=True, null=True)
	Frasco11 = models.DateField(blank=True, null=True)
	Frasco12 = models.DateField(blank=True, null=True)
	Frasco13 = models.DateField(blank=True, null=True)
	Frasco14 = models.DateField(blank=True, null=True)
	Frasco15 = models.DateField(blank=True, null=True)
	Frasco16 = models.DateField(blank=True, null=True)
	Frasco17 = models.DateField(blank=True, null=True)
	Frasco18 = models.DateField(blank=True, null=True)
	Frasco19 = models.DateField(blank=True, null=True)
	Frasco20 = models.DateField(blank=True, null=True)
	Frasco21 = models.DateField(blank=True, null=True)
	Frasco22 = models.DateField(blank=True, null=True)
	Frasco23 = models.DateField(blank=True, null=True)
	Frasco24 = models.DateField(blank=True, null=True)
	Frasco25 = models.DateField(blank=True, null=True)

	def __str__(self):
		return self.nombre + ' ' + self.apellidos
