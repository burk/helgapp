from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User

class Application(models.Model):
    user = models.ForeignKey(User)
    applied = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128)
    leader = models.IntegerField()
    about = models.TextField()
    accepted = models.NullBooleanField(null=True)

