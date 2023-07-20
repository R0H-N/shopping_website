from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class category(models.Model):
    name = models.CharField(max_length= 255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(category,related_name='items',on_delete=models.CASCADE)
    name = models.CharField(max_length= 255)
    image = models.ImageField(upload_to='item_image',null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    price = models.FloatField()
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
