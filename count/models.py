from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    SEXES = (
        ('femme', 'Femme'),
        ('homme', 'Homme'),
    )
    user = models.ForeignKey(User, related_name="client", on_delete=models.CASCADE)
    telephone = models.CharField(max_length=20, unique=True,)
    sexe = models.CharField(max_length=12, choices=SEXES)
    date_naiss = models.DateField(editable=True)
    pays = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

