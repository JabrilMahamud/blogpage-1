from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('timeline/', views.timeline, name='timeline'),
    path('timeline/<int:id>/', views.timeline, name='timeline_post'),
    path('create_post/', views.create_post, name='create_post'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)