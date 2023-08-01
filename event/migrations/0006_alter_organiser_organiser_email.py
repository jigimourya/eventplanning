# Generated by Django 4.0.8 on 2023-07-12 17:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_alter_organiser_organiser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organiser',
            name='organiser_email',
            field=models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator(message='Invalid Email')]),
        ),
    ]