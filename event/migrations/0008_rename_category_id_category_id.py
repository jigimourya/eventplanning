# Generated by Django 4.0.8 on 2023-07-20 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_id',
            new_name='id',
        ),
    ]
