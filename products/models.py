from django.db import models

class Productz(models.Model):
    name = models.CharField(max_length=50)
    mugshot = models.ImageField(upload_to='products')
    description = models.TextField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    rate = models.IntegerField(max_length=1)
    quatinty = models.IntegerField(default=1)
    tag = models.CharField()
    def __str__(self):
        return str(self.name)
    
    