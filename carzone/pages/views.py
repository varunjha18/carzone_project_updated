from django.shortcuts import render
from .models import Team
from cars.models import Car

# Create your views here.
teams=Team.objects.all()
all_cars=Car.objects.order_by('-created_date')



def home(request):
    featured_cars=Car.objects.order_by('-created_date').filter(is_featured=True)
    make_fields=Car.objects.values_list('car_title',flat=True).distinct()
    model_fields=Car.objects.values_list('model',flat=True).distinct()
    year_fields=Car.objects.values_list('year',flat=True).distinct()
    city_fields=Car.objects.values_list('city',flat=True).distinct()
    body_fields=Car.objects.values_list('body_style',flat=True).distinct()
   
   
    data={"teams":teams,
        "featured_cars":featured_cars,
        'all_cars':all_cars,
        'make_fields':make_fields,
        'model_fields':model_fields,
        'year_fields':year_fields,
        'city_fields':city_fields,
        'body_fields':body_fields,
    }

    return render(request,"pages/home.html",data)


def about(request):
    data={"teams":teams,}
    return render(request,"pages/about.html",data)


def services(request):
    return render(request,"pages/services.html")


def contact(request):
    return render(request,"pages/contact.html")
