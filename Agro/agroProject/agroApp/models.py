from django.db import models

# Create your models here.
class RegistroActividad(models.Model):
    responsable = models.CharField(max_length=100)
    actividad = models.TextField()
    parcela = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.responsable} - {self.parcela}"
    class Meta:
        verbose_name = "Registro de actividad"
        verbose_name_plural = "Registros de actividades"
        ordering = ['-fecha_registro']