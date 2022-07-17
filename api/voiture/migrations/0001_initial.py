# Generated by Django 4.0 on 2021-12-22 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=120)),
                ('matricule', models.CharField(max_length=120)),
                ('kilometrages', models.CharField(max_length=120)),
                ('assurance', models.CharField(max_length=120)),
                ('vignette', models.CharField(max_length=120)),
                ('personnelle', models.BooleanField(default=False)),
            ],
        ),
    ]
