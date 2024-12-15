from django.contrib import admin
from .models import News, PrayerRequest, Image, ImageCategory, Video, Registration
# Register your models here.
admin.site.register(News)
admin.site.register(PrayerRequest) # register
admin.site.register(Image) # register
admin.site.register(ImageCategory) # register
admin.site.register(Video)
admin.site.register(Registration)