from django.shortcuts import render
#from django.http import HttpResponse
from .models import Posts

# posts = [
#     {
#         'author': 'Abhilash',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2020'
#      },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 28, 2018'
     
#      }
# ]


# Create your views here.
def home(request):
    context = {
            'posts' : Posts.objects.all()
        }
    
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title' : 'About'})

