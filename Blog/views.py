from django.shortcuts import render,HttpResponse
from Blog.models import Homestay
# Create your views here.
def index(request):
    
    return render(request,'index.html')

def homestay(request):
    
    homestay=Homestay.objects.all
    context={'homestay':homestay}
    return render(request,'homestay.html',context)

def blog(request):
    
    return render(request,'blog.html')

def contact(request):
    
    return render(request,'contact.html')


def homestays(request,slug):

    home = Homestay.objects.filter(slug=slug)
    
    return render(request,'homestays.html')

