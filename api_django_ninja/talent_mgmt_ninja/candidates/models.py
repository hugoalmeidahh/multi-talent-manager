from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    status = models.CharField(
        max_length=50, 
        choices=[
            ('available', 'Available'), 
            ('unavailable', 'Unavailable')
		])
    skills = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name