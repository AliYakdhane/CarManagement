# Generated by Django 4.0 on 2021-12-29 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voiture', '0009_alter_voiture_vignette'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voiture',
            name='assurance',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='voiture',
            name='vignette',
            field=models.CharField(max_length=120),
        ),
    ]