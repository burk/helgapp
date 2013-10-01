from django.db import models

class Snap(models.Model):
    filename = models.CharField(primary_key=True, max_length=128)
    username = models.CharField(max_length=128)
    downloaded = models.DateTimeField(auto_now_add=True)

