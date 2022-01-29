from turtle import title
from django.shortcuts import redirect, render


from .models import Category,Posts
from .forms import InsertCategory,InsertPosts
# Create your views here.

def Cat(r):
    InsertCat=InsertCategory(r.POST or None)
    if r.method == "POST":
        InsertCat.save()
        return redirect(Post)
   

def Post(r):
    InsertPost=InsertPosts(r.POST or None)
    InsertCat=InsertCategory(r.POST or None)
    if r.method == "POST":
        InsertPost.save()
        return redirect(Post)
    else:
        data={"Insertpost":InsertPost,
        "Insertcat":InsertCat,
        "CallingPosts":Posts.objects.all(),
        "CallingCat":Category.objects.all(),
        }
        return render (r, "index.htm",data)

def search(r):
    InsertPost=InsertPosts(r.POST or None)
    InsertCat=InsertCategory(r.POST or None)
    data={"CallingPosts":Posts.objects.filter(title__icontains=r.GET.get("search")),
    "Insertpost":InsertPost,
    "Insertcat":InsertCat,
    "CallingCat":Category.objects.all(),
    }
    return render(r,"index.htm",data)

def selectCat(r,id):
    a=Category.objects.get(pk=id)
    InsertPost=InsertPosts(r.POST or None)
    InsertCat=InsertCategory(r.POST or None)
    data={"CallingPosts":Posts.objects.filter(cat_id=a),
    "Insertpost":InsertPost,
    "Insertcat":InsertCat,
    "CallingCat":Category.objects.all(),
    }
    return render(r,"index.htm",data)

def view(r,id):
    a=Posts.objects.get(pk=id)
   
    data={"i":a,
    "CallingCat":Category.objects.all(),
    }
    return render(r,"view.htm",data)