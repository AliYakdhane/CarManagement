from django.db import models

def upload_path(instance, filename):
    return 'posts/{filename}'.format(filename=filename)

class Voiture(models.Model):
    marque = models.CharField(max_length=120)
    matricule = models.CharField(max_length=120)
    kilometrages = models.CharField(max_length=120)
    assurance = models.DateField()
    vignette = models.DateField()
    personnelle = models.BooleanField(default=False)
    travail = models.BooleanField(default=True)
  
    def _str_(self):
        return self.marque