# Generated by Django 4.0.1 on 2022-02-04 12:20

from django.db import migrations, models
import voiture.models


class Migration(migrations.Migration):

    dependencies = [
        ('voiture', '0012_alter_voiture_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voiture',
            name='cover',
            field=models.ImageField(upload_to=voiture.models.upload_path, verbose_name='Cover'),
        ),
    ]
