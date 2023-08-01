# Generated by Django 4.0.8 on 2023-07-12 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_organiser_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='organiser',
            name='thumbnail',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='organiser',
            name='avatar',
            field=models.ImageField(upload_to='media/'),
        ),
    ]