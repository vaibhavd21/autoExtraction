from django.db import models

HOST_CHOICES= [
    ('TeamSupport', 'TeamSupport'),
    ('QuickBase', 'QuickBase'),
    ('Snow', 'Snow'),
    ('Workday', 'Workday'),
    ]
# Create your models here.
class data(models.Model):
    
    host = models.CharField(max_length=100,choices=HOST_CHOICES, default='TeamSupport')
    product = models.CharField(max_length=300)
    startDate = models.DateField()
    endDate = models.DateField()
    request_at = models.DateTimeField(auto_now_add=True)

