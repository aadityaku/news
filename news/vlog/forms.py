from dataclasses import field, fields
from pyexpat import model
from django.forms import ModelForm
from .models import Category,Posts


class InsertCategory(ModelForm):
    class Meta:
        model=Category
        fields=["cat_title"]

class InsertPosts(ModelForm):
    class Meta:
        model=Posts
        fields=["title","author","content","cat_id","date"]