from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('projects/', views.projects, name='projects'),
    path('blog_list/', views.blog_list, name='blog_list'),
    path('team/', views.team, name='team'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),  # Detail page

]
