from django.db import models

class EmailSubscriber(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField()

class Deneme(models.Model):
    name = models.CharField(max_length=100)
    nachname = models.CharField(max_length=100)
    age = models.IntegerField()


