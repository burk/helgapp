from django.db import models

class Snap(models.Model):
    filename = models.CharField('124')
    downloaded = models.DateTimeField('date downloaded')

