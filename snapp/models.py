from django.db import models

class Snap(models.Model):
    filename = models.CharField(max_length=124)
    downloaded = models.DateTimeField('date downloaded')

