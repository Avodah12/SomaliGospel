from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('gallery/', views.image_gallery, name='gallery'),
    path('register/', views.register, name='register'),
    
    path('prayer_request/', views.prayer_request, name='prayer_request'),
    path('registration-success/', views.registration_success, name='registration_success'),
    
    path('prayer-request/success/', views.prayer_request_success, name='prayer_request_success'),]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)