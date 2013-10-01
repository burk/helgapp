from django.db import models

class Snap(models.Model):
    filename = models.CharField()
    downloaded = models.DateTimeField('date downloaded')

