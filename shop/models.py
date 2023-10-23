from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from count.models import Client


# Create your models here.
class Categorie(models.Model):
    libelle = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.libelle
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.libelle)
        return super().save(*args, **kwargs)

class SousCategorie(models.Model):
    category = models.ForeignKey(Categorie, related_name="categories", on_delete=models.CASCADE)
    libelle = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    slug = models.SlugField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.libelle
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.libelle)
        return super().save(*args, **kwargs)

class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="commandes")
    code = models.CharField(max_length=40, unique=True)
    montant = models.DecimalField(max_digits=6, decimal_places=2)
    mode_payement = models.CharField(max_length=60, verbose_name="Mode de payement", null=True)
    is_valid = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.client.username
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.client.username)
        return super().save(*args, **kwargs)

class Produit(models.Model):
    libelle = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True, upload_to="IMG")
    prix_unitaire = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField()
    description = models.TextField()
    sous_categorie = models.ForeignKey(SousCategorie, on_delete=models.CASCADE, related_name='appartient')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.libelle)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.libelle

class ProduitCommande(models.Model):
    produit = models.ManyToManyField(Produit, related_name="produits")
    commande = models.ManyToManyField(Commande, related_name="commandes")
    quantity = models.IntegerField(default=0, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

class NewCommande(models.Model):
    items = models.CharField(null=True, blank=True, max_length=255)
    sommeTotal = models.CharField(null=True, blank=True, max_length=12)
    prenom = models.CharField(max_length=60)
    nom = models.CharField(max_length=60)
    pays = models.CharField(max_length=60)
    ville = models.CharField(max_length=100)
    lieu = models.CharField(max_length=60)
    email = models.EmailField(max_length=60, unique=True)
    phone = models.CharField(max_length=18, unique=True)
    codepostal = models.CharField(max_length=60)
    mobile = models.CharField(max_length=20)
    password = models.CharField(max_length=20, null=True, blank=True)

class Blog (models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)
    categgorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    auther = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="IMG")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at', '-updated_at']

    
