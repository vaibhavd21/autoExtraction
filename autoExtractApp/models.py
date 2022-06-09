from django.db import models

# Create your models here.
class data(models.Model):
    host = models.CharField(max_length=100)
    product = models.CharField(max_length=300)
    startDate = models.DateField()
    endDate = models.DateField()
    request_at = models.DateTimeField(auto_now_add=True)

