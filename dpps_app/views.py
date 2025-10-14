from django.shortcuts import render, get_object_or_404,redirect
from .forms import User_TestimonialForm  
from .models import BlogPost, Service, Team,FAQ,User_Testimonial

from .models import FAQ

# views.py (update your home and services views to include the form instance)
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User_Testimonial
from .forms import User_TestimonialForm


def home(request):
    service = Service.objects.all()[:3]
    team = Team.objects.all()
    testimonials = User_Testimonial.objects.all()
    form = User_TestimonialForm()  # Hapa ndio fix: Always create form    
    blog_posts = BlogPost.objects.all()
    faqs = FAQ.objects.all()

    context = {
        'service': service,
        'team': team,
        'form': form,
        'testimonials': testimonials,
        'blog_posts': blog_posts,
        'faqs': faqs,
    }
    return render(request, 'index.html', context)

def about(request):
    service = Service.objects.all()[:3]
    team = Team.objects.all()
    testimonials = User_Testimonial.objects.all()
    blog_posts = BlogPost.objects.all()
    faqs = FAQ.objects.all()

    context = {
        'service': service,
        'team': team,
        'form': form,
        'testimonials': testimonials,
        'blog_posts': blog_posts,
        'faqs': faqs,
    }

    return render(request, 'about.html',context)

def services(request):
    service = Service.objects.all()
    team = Team.objects.all()
    testimonials = User_Testimonial.objects.all()
    form = User_TestimonialForm()  # Hapa ndio fix: Always create form    
    blog_posts = BlogPost.objects.all()
    faqs = FAQ.objects.all()

    context = {
        'service': service,
        'team': team,
        'form': form,
        'testimonials': testimonials,
        'blog_posts': blog_posts,
        'faqs': faqs,
    }
    return render(request, 'service.html',context)

def projects(request):
    return render(request, 'projects.html')

def team(request):
    service = Service.objects.all()[:3]
    team = Team.objects.all()
    testimonials = User_Testimonial.objects.all()
    blog_posts = BlogPost.objects.all()
    faqs = FAQ.objects.all()

    context = {
        'service': service,
        'team': team,
        'testimonials': testimonials,
        'blog_posts': blog_posts,
        'faqs': faqs,
    }
    return render(request, 'team.html',context)

def faq(request):
    service = Service.objects.all()[:3]
    team = Team.objects.all()
    testimonials = User_Testimonial.objects.all()
    blog_posts = BlogPost.objects.all()
    faqs = FAQ.objects.all()

    context = {
        'service': service,
        'team': team,
        'testimonials': testimonials,
        'blog_posts': blog_posts,
        'faqs': faqs,
    }
    return render(request, 'Questions.html',context)

def contact(request):
    return render(request, 'contact.html')

def blog_list(request):
    service = Service.objects.all()[:3]
    team = Team.objects.all()
    testimonials = User_Testimonial.objects.all()
    blog_posts = BlogPost.objects.all()
    faqs = FAQ.objects.all()

    context = {
        'service': service,
        'team': team,
        'testimonials': testimonials,
        'blog_posts': blog_posts,
        'faqs': faqs,
    }
    return render(request, 'blog.html',context)

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
   
    service = Service.objects.all()[:3]
    team = Team.objects.all()
    testimonials = User_Testimonial.objects.all()
    blog_posts = BlogPost.objects.all()
    faqs = FAQ.objects.all()

    context = {
        'service': service,
        'team': team,
        'testimonials': testimonials,
        'blog_posts': blog_posts,
        'faqs': faqs,
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




    service = Service.objects.all()[:3]
    team = Team.objects.all()
    testimonials = User_Testimonial.objects.all()
    blog_posts = BlogPost.objects.all()
    faqs = FAQ.objects.all()

    context = {
        'service': service,
        'team': team,
        'testimonials': testimonials,
        'blog_posts': blog_posts,
        'faqs': faqs,
    }

    return render(request, 'contact.html', {'form': form}, context)

# def submit_testimonial(request):
#     if request.method == 'POST':
#         form = User_TestimonialForm(request.POST)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.image.store()  # Manually store if not auto-stored (optional, but safe)
#             instance.save()
#             messages.success(request, 'Thank you! Your testimonial has been submitted.')
#         else:
#             messages.error(request, 'Please correct the errors below.')
#         return redirect(request.META.get('HTTP_REFERER', 'home'))
#     return redirect('home')



# views.py (update submit_testimonial to handle AJAX and return JSON)
from django.contrib import messages
from django.http import JsonResponse  # Add this import

def submit_testimonial(request):
    if request.method == 'POST':
        form = User_TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # Check if AJAX
                return JsonResponse({'status': 'success', 'message': 'Review submitted successfully!'})
            messages.success(request, 'Review submitted successfully!')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                errors = form.errors.as_json()
                return JsonResponse({'status': 'error', 'errors': errors}, status=400)
            messages.error(request, 'Please correct the errors below.')
        return redirect(request.META.get('HTTP_REFERER', 'home'))
    return redirect('home')