from django.db import models
from django.db.models import JSONField


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    height = models.IntegerField()
    weight = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    evolutions = models.CharField(max_length=100, null=True)
    base_stats = JSONField(null=True, default=dict)
    image = models.CharField(max_length=100, null=True)

