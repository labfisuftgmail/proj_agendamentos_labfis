from django.db import models

# Create your models here.
class Area(models.Model):
    nome = models.CharField(max_length=255, null=False, unique=True)
    
    class Meta:
        verbose_name = "Área"

    def __str__(self):
        return self.nome

class Experimento(models.Model):
    nome = models.CharField(max_length=255, null=False)
    descricao = models.TextField(blank=True)
    area = models.ForeignKey(Area, default=1 ,on_delete=models.SET_DEFAULT)

    def __str__(self):
        return f"({self.area.nome}) {self.nome}"

class Arquivo(models.Model):
    nome = models.FileField(upload_to='uploads/', max_length=255, null=False, unique=True, verbose_name='Arquivo')
    decricao = models.CharField(max_length=255, verbose_name="Descrição Curta", null=True, default='')
    experimento = models.ForeignKey(Experimento, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.nome
