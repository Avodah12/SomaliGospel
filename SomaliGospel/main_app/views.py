from django.shortcuts import redirect, render

from main_app.forms import PrayerRequestForm
from .models import Image, News, ImageCategory, Video

# Create your views here.
def home(request):
    news = News.objects.all()
    
    if request.method == 'POST':
        form = PrayerRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prayer_request_success')  # Redirect to a success page or reload home
    else:
        form = PrayerRequestForm()
    
    context = {'news': news, 'form': form}
    return render(request, 'main_app/home.html', context)

def news(request):
    news = News.objects.all()
    context = {'news': news}
    return render(request, 'main_app/news.html', context)



def prayer_request_success(request):
    return render(request, 'main_app/prayer_request_success.html')  # Create a simple success page




def image_gallery(request):
    # Get all categories
    categories = ImageCategory.objects.all()

    # If a category is selected, filter images by category
    selected_category = request.GET.get('category')  # Get the category from the query parameter

    if selected_category:
        # Filter images based on the selected category
        images = Image.objects.filter(category__id=selected_category)
    else:
        # Show all images if no category is selected
        images = Image.objects.all()
    
    # Get all videos
    videos = Video.objects.all()

    # Pass the categories, filtered images, and videos to the template
    return render(request, 'main_app/gallery.html', {'categories': categories, 'images': images, 'videos': videos})
def prayer_request(request):
    if request.method == 'POST':
        form = PrayerRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prayer_request_success')  # Redirect to a success page or reload home
    else:
        form = PrayerRequestForm()
    
    return render(request, 'main_app/prayer_request_page.html', {'form': form})
from django.shortcuts import render, redirect
from .forms import RegistrationForm




# views.py (add this view)
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')  # Redirect to the success page
        else:
            # In case of form errors, return the form with error messages
            return render(request, 'main_app/register.html', {'form': form})
    else:
        form = RegistrationForm()

    return render(request, 'main_app/register.html', {'form': form})


def registration_success(request):
    return render(request, 'main_app/registration_success.html')


