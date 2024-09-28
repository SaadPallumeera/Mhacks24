from django.db import models


class Query(models.Model):
    input = models.CharField(max_length=100)

    def __str__(self):
        return self.title
# Create your models here.

