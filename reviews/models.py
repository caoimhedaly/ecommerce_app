from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.


class Review(models.Model):
    
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='reviews', null=False, on_delete=models.PROTECT) 
    product= models.ForeignKey(Product, related_name= 'reviews', null=False, on_delete=models.PROTECT)
  
    def __str__(self):
        return self.title
