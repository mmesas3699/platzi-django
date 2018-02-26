from django.db import models

# Create your models here.

class Country(models.Model):
    CODES_CHOICES = (
        ('Colombia', 'CO'),
        ('Estados Unidos', 'USA'),
        ('Mexico', 'MX')
    )

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=3, choices=CODES_CHOICES)
    # code = models.CharField(max_length=3)

    # Si quiero que el campo code tome solo ciertos datos dados (que usuario no inserte lo que quiera, si no 
    # lo que se le da a escoger):
    # code = models.CharField(max_length=3, choices=CODES_CHOICES)
