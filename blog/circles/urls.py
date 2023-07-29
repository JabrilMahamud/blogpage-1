from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('timeline/', views.timeline, name='timeline'),
    path('timeline/<int:id>/', views.timeline, name='timeline_post'),

]
