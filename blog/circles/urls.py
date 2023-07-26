from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('template/', views.template_page, name='template_page'),
    path('timeline/', views.timeline, name='timeline'),
    path('timeline/<int:id>/', views.timeline, name='timeline_post'),

]
