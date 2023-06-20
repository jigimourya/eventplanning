# Generated by Django 4.0.8 on 2023-06-20 08:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_alter_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organiser',
            name='user_id',
        ),
        migrations.AddField(
            model_name='organiser',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organiser',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]