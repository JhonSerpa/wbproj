from django.db import models


class ngolo(models.Model):
    nem = models.CharField(max_length=100)

    def __str__(self):
        return self.nem

