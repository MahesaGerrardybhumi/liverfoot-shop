from django.db import models
from django.db import models

class Product(models.Model):
    product = [
        ("Sepatu Futsal", "sepatu futsal"),
        ("Sepatu Bola", "sepatu bola"),
    ]
    
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=20, choices=product, default="update")
    product_views = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    @property
    def is_product_hot(self):
        return self.product_views > 20

    def increment_views(self):
        self.product_views += 1
        self.save()
# Create your models here.
