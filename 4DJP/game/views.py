from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-created_at'),
    return render(request,'core/index.html',{'posts':posts})