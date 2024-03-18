from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Date de naissance')
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    occupation = models.CharField(max_length=100, blank=True, null=True, verbose_name='Occupation')
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Téléphone')
    address = models.CharField(max_length=100, blank=True, null=True, verbose_name='Adresse')
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name='Ville')
    country = models.CharField(max_length=100, blank=True, null=True, verbose_name='Pays')
    postal_code = models.CharField(max_length=100, blank=True, null=True, verbose_name='Code postal')
    education = models.CharField(max_length=200, blank=True, null=True, verbose_name='Education')
    experience = models.TextField(blank=True, null=True, verbose_name='Expérience')
    skills = models.CharField(max_length=200, blank=True, null=True, verbose_name='Compétences')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return f"Profile pour l'utilisateur {self.user.username}"

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()
