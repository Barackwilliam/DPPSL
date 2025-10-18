from django.urls import path
from . import views
from .views import submit_testimonial
from django.contrib.auth import views as auth_views

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


    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Dashboard and profile URLs
    path('dashboard/', views.dashboard, name='dashboard'),
    path('complete-profile/', views.complete_profile, name='complete_profile'),
    path('download-certificate/', views.download_certificate, name='download_certificate'),
    
    # Training participants list
    path('training/<int:training_id>/participants/', views.training_participants, name='training_participants'),
]

