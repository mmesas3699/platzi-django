from django.db import models

# Create your models here.


class ActiveManager(models.Manager):
    """
    Creacion de un Manager para que cuando se use solo traiga
    los Countries activos. Para que funcione hay que colocar en
    los modelos que van a usar este Manager la variable:
    active_manager = ActiveManager
    """

    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class Country(models.Model):
    CODES_CHOICES = (
        ('Colombia', 'CO'),
        ('Estados Unidos', 'USA'),
        ('Mexico', 'MX')
    )

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=3, choices=CODES_CHOICES)
    # code = models.CharField(max_length=3)
    continent = models.ForeignKey(
        'continents.Continent',
        on_delete=models.CASCADE
    )
    active = models.BooleanField(default=True)
    active_manager = ActiveManager()
    objects = models.Manager()

    def __str__(self):
        return self.name

    # Si quiero que el campo code tome solo ciertos datos dados (que el usuario
    # no inserte lo que quiera, si no lo que se le da a escoger):
    # code = models.CharField(max_length=3, choices=CODES_CHOICES)
