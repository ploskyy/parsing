from django.db import models
from django.utils import timezone

class Flat(models.Model):
    id_avito = models.CharField(max_length=120, default='unknown')
    title = models.CharField(max_length=120, default='unknown')
    price = models.CharField(max_length=120, default='unknown')
    address = models.CharField(max_length=120, default='unknown')
    url = models.CharField(max_length=120, default='unknown')
    tel = models.CharField(max_length=120, default='unknown')
    date_avito = models.CharField(max_length=120, default='unknown')

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.title
