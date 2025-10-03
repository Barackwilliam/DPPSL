from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Service, Team, User_Testimonial
from .models import FAQ

def home(request):
    service = Service.objects.all()[:3]
    team = Team.objects.all()
    testimonial = User_Testimonial.objects.all()
    blog_posts = BlogPost.objects.all()
    faqs = FAQ.objects.all()

    context = {
        'service': service,
        'team': team,
        'testimonial': testimonial,
        'blog_posts': blog_posts,
        'faqs': faqs,
    }
    return render(request, 'index.html', context)

def about(request):
    testimonial = User_Testimonial.objects.all()
    team = Team.objects.all()
    service = Service.objects.all()[:3]

    context ={
        'service':service,
        'team':team,
        'testimonial':testimonial,
    }

    return render(request, 'about.html',context)

def services(request):
    service = Service.objects.all()
    testimonial = User_Testimonial.objects.all()



    context ={
        'service':service,
        'testimonial':testimonial,

    }
    return render(request, 'service.html',context)

def projects(request):
    return render(request, 'projects.html')

def training(request):
    return render(request, 'training.html')

def contact(request):
    return render(request, 'contact.html')

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    context = {
        'post': post
    }
    return render(request, 'blog_detail.html', context)
