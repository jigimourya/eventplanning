# Generated by Django 4.0.8 on 2023-06-20 10:48

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organiser',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('user_id', models.BigIntegerField(default=0)),
                ('event_type', models.CharField(choices=[('Seminar', 'Seminar'), ('Webinar', 'Webinar'), ('Hackathon', 'Hackathon'), ('Workshop', 'Workshop'), ('Competition', 'Competition'), ('Visit', 'Visit'), ('Camp', 'Camp'), ('Fest', 'Fest'), ('Cultural festival', 'Cultural Festival'), ('Party', 'Party')], max_length=50)),
                ('name_of_event', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=200)),
                ('department', models.CharField(choices=[('choose', '--Choose your school--'), ('SSET', 'Sharda School of Engineering and Technology'), ('SSAHS', 'Sharda School of Allied Health Sciences'), ('SSBSR', 'Sharda School of Basic Sciences and Research'), ('SSMFE', 'Sharda School of Media, Film and Entertainment')], max_length=50)),
                ('for_batch', models.CharField(choices=[('first year', 'First year (1st Year)'), ('second year', 'Second year (2nd Year)'), ('third year', 'Third year (3rd Year)'), ('fourth year', 'Fourth year (4th Year)'), ('fifth year', 'Fifth year (5th Year)')], max_length=50)),
                ('date', models.DateField()),
                ('venue', models.CharField(max_length=200)),
                ('time', models.TimeField()),
                ('mode', models.CharField(choices=[('online', 'Online'), ('offline', 'Offline')], max_length=50)),
                ('organiser_name', models.CharField(max_length=200)),
                ('organiser_phone', models.CharField(max_length=200)),
                ('organiser_email', models.CharField(max_length=200)),
                ('last_date_to_register', models.DateField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_school', models.CharField(choices=[('choose', '--Choose your school--'), ('SSET', 'Sharda School of Engineering and Technology'), ('SSAHS', 'Sharda School of Allied Health Sciences'), ('SSBSR', 'Sharda School of Basic Sciences and Research'), ('SSMFE', 'Sharda School of Media, Film and Entertainment')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(max_length=20)),
                ('systemid', models.CharField(max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
