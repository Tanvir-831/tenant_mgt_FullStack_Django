from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Building(models.Model):
    name = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    District = models.CharField(max_length=100)
    post_code = models.CharField(max_length=10)
    total_flat = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    building_image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name
    

class Flat(models.Model):
    number = models.CharField(max_length=10)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    bedroom = models.IntegerField()
    washroom = models.IntegerField()
    kitchen = models.IntegerField()
    balcony = models.IntegerField()
    flat_area = models.FloatField()
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='tenant_flat')
    rent = models.FloatField()

    def __str__(self):
        return self.number


