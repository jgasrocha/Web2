# Generated by Django 5.1.1 on 2024-09-28 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_teacher',
        ),
    ]
