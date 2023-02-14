from django.db import models

# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=255, null=False, unique=True)

    def __str__(self):
        return self.nome

class Docente(models.Model):
    STATUS_CHOICE = (
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo'),
    )
    nome = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, unique=True)
    cursos = models.ManyToManyField(Curso, blank=True)
    status = models.CharField(
        max_length=32,
        choices=STATUS_CHOICE,
        default='Ativo'
    )

    def __str__(self):
        return self.nome
