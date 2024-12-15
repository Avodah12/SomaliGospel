from django.db import models
from django.utils.text import slugify

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']


class PrayerRequest(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    prayer_request = models.TextField(blank=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name}'s Prayer Request"
    


class ImageCategory(models.Model):
    name = models.CharField(max_length=100, unique=True) 

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='images/')  # The image file (stored in a folder called 'images/')
    category = models.ForeignKey(ImageCategory, on_delete=models.CASCADE, related_name='images')  # Linking image to a category
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the image was added
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the image was last updated


class Video(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='videos/')  # Store videos in the 'videos' directory
    created_at = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='video_thumbnails/', null=True, blank=True)

    def __str__(self):
        return self.title
    

class Registration(models.Model):
    CATEGORY_CHOICES = [
        ('membership', 'Membership'),
        ('trainings', 'Trainings'),
        ('fellowship', 'Fellowship'),
    ]
    
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    additional_details = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.category}"