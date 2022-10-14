#archivo para enviar una señal de queluego que se cree un usuario automaticamente se cree un perfil

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile,Country
from django.dispatch import receiver

@receiver(post_save,sender=User) #decorador para llamar a la funcion
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def create_country(sender, instance, created, **kwargs):
    if created:
        Country.objects.create(user=instance)