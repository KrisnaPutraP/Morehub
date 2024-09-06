from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=100)
    description = models.TextField()
    quantity = models.IntegerField()
    category = models.CharField(max_length=100)
    featured = models.BooleanField()

    def __str__(self):
        return self.name
