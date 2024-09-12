from django.db import models

class Query(models.Model):
    qyery_text = models.CharField(max_length=200)
    counter = models.PositiveIntegerField(default=0)