from django.db import models

class ClmAttributes(models.Model):
    name_attr = models.CharField(max_length=30)
    clm_attr = models.CharField(max_length=30)

class MainLinks(models.Model):
    name_link = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
