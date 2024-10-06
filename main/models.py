import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=100)
    description = models.TextField()
    quantity = models.IntegerField()
    category = models.CharField(max_length=100)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
