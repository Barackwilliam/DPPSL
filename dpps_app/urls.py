from django.urls import path
from . import views
from .views import submit_testimonial

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('projects/', views.projects, name='projects'),
    path('blog_list/', views.blog_list, name='blog_list'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('submit-testimonial/', submit_testimonial, name='submit_testimonial'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),  # Detail page

]
