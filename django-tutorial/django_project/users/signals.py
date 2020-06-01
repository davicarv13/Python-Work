from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

"""
!!!
Quando um usuário é salvo então dispare o signal post_save
O signal será recebido por @receiver e este @receiver é a função
definida abaixo
A função então recebe todos os argumentos que o signal post_save 
mandou para ela. Um deles é a instância do user que foi criado, outro 
é o parâmetro que define se um user foi criado (created)
Se o user foi criado então, então crie um profile e atrele ele a instância 
de usuário
!!!
"""

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

#Esta função é disparada quando um usuário é salvo
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()

post_save.connect(save_profile, sender=User)


