from turtle import title
from django.db import models

# Create your models here.
class Category(models.Model):
    cat_title=models.CharField(max_length=200)
    
    def __str__(self):
        return self.cat_title

class Posts(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    content=models.TextField(blank=False)
    cat_id=models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    date=models.DateField()

    def __str__(self):
        return self.title