# Generated by Django 4.0.8 on 2023-07-11 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_rename_date_organiser_event_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='organiser',
            name='avatar',
            field=models.ImageField(default='shardians2.jpg', upload_to='staticfiles/'),
        ),
    ]
