# """
# Modulos importados para lanzar los signals
# """
# import logging
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import User, Profile



# """
# Signal lanzada antes de crear un User
# """
# logger = logging.getLogger(__name__)
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     logger.info("Creando perfil de:  %d", instance.username)
#     if created:
#         Profile.objects.create(user=instance, description='Nuevo usuario')

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
