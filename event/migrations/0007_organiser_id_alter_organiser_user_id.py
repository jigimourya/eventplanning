# Generated by Django 4.0.8 on 2023-06-20 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_remove_organiser_id_remove_organiser_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='organiser',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='organiser',
            name='user_id',
            field=models.CharField(max_length=200),
        ),
    ]