from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    skills = models.TextField()
    status = models.CharField(max_length=50, choices=[
        ('disponivel', 'Disponível'),
        ('indisponivel', 'Indisponível')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
