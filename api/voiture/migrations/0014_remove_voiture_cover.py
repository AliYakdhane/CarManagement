# Generated by Django 4.0.1 on 2022-02-04 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voiture', '0013_alter_voiture_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voiture',
            name='cover',
        ),
    ]