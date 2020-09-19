#define the logic and control for request and HTTP responses
from django.shortcuts import  render
from .models import Post
#dummy data
#list of dictionaries


def home(request):
    #context dictionary is taking the "posts" list as value
    context = {
        'posts' : Post.objects.all() ,
        'title' : 'HOME'
    }
    return render(request,'blog/home.html',context)


