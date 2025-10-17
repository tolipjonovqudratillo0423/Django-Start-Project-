from django.shortcuts import render

# Create your views here.
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-created_at'),
    return render(request,'core/index.html',{'posts':posts})