from django.shortcuts import render, get_object_or_404,redirect

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

from django.contrib import messages
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully! We'll get back to you soon.")
            return redirect('contact')  # Rudisha kwenye ukurasa wa contact
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
