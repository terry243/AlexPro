from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
class utilisateur(models.Model):
    name = models.CharField(max_length=70)
    type= models.CharField(max_length=70)
    position= models.CharField(max_length=2)
    adresse= models.CharField(max_length=100)
    email= models.CharField(max_length=255)
    password= models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Lignebdgetaire(models.Model):
    origine_choice = (
        ('BA','BA'),
        ('DON','DON'),
        ('Recette','RECETTE')
    )
    nom_origine_choice = (
        ('OBC','OBC'),
        ('BEAC','BEAC'),
        ('infos','Recuperation des diplomes')
    )
    name = models.CharField(max_length=70)
    origine= models.CharField(max_length=70,choices=origine_choice,default='BA')
    nomorigine= models.CharField(max_length=50,choices=nom_origine_choice,default='OBC')
    adresse= models.CharField(max_length=100)
    montant= models.CharField(max_length=255)

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_client = models.BooleanField(default=True)
    is_delegue = models.BooleanField(default=False)
    
    

class Produit(models.Model):
    categorie_choices = (
        ('P','Pantalon'),
        ('H','Habit'),
        ('C','Chaussure'),
        ('ch','Chemise')
    )
    nom = models.CharField(max_length=50,unique=True)
    description = models.TextField()
    cathegorie = models.CharField(max_length=100,choices=categorie_choices,default='P')
    prix= models.DecimalField(max_digits=100000,decimal_places=3)
