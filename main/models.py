from django.db import models
from django.db import models

class Product(models.Model):
    product = [
        ("Nike Mercurial", "nike mercurial"),
        ("Nike Tiempo", "nike tiempo"),
        ("Nike Phantom", "nike phantom"),
        ("Ortuseight Catalyst", "ortuseight catalyst"),
        ("Adidas F50", "adidas f50"),
        ("Adidas Predator", "adidas predator"),
    ]
    
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=20, choices=product, default="update")
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    @property
    def is_news_hot(self):
        return self.news_views > 20
        
    def increment_views(self):
        self.news_views += 1
        self.save()
# Create your models here.
