from django.db import models
from authemail.models import EmailUserManager, EmailAbstractUser


class CustomUser(EmailAbstractUser):
    # Custom fields
    first_name = models.CharField("Nombres", max_length=150, null=False)
    last_name = models.CharField(
        "Apellido Paterno", max_length=150, null=False)
    apellido_materno = models.CharField(
        "Apellido Materno", max_length=100, null=True, blank=True)
    matricula = models.CharField(
        "Matricula", max_length=8,null=False,blank=False)
    
    # Required
    objects = EmailUserManager()
