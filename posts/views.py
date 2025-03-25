# from django.shortcuts import render
# from .models import Post 

# def post_list(request):
#     post=Post.objects.all()
#     return render(request,"post_list.html",{"post":post})




# # Create your views here.
from django.views.generic import ListView 
from .models import Post

class PostL(ListView):
    model=Post 
    template_name="posts_list.html"
