# Generated by Django 4.2.11 on 2024-03-17 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_address_profile_city_profile_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='education',
            field=models.TextField(blank=True, null=True, verbose_name='Education'),
        ),
    ]