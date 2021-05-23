from django.shortcuts import get_object_or_404, render
from cars.models import Car
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
all_cars=Car.objects.order_by('-created_date')
def cars(request):
    paginator=Paginator(all_cars,2)
    page=request.GET.get('page')
    paged_cars=paginator.get_page(page)
    
    data={
        'all_cars':paged_cars,
    }
    return render(request,"cars/cars.html",data)

def car_detail(request,id):
    single_car= get_object_or_404(Car,pk=id)
    data={
        "single_car":single_car,
    }
    return render(request,"cars/car_detail.html",data)



def search(request):
    all_cars=Car.objects.order_by('-created_date')
    make_fields=Car.objects.values_list('car_title',flat=True).distinct()
    model_fields=Car.objects.values_list('model',flat=True).distinct()
    year_fields=Car.objects.values_list('year',flat=True).distinct()
    city_fields=Car.objects.values_list('city',flat=True).distinct()
    body_fields=Car.objects.values_list('body_style',flat=True).distinct()
    transmission_fields=Car.objects.values_list('transmission',flat=True).distinct()
    
    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        if keyword:
            all_cars=all_cars.filter(description__icontains=keyword)
    
    if 'make' in request.GET:
        make=request.GET['make']
        if make:
            all_cars=all_cars.filter(car_title__icontains=make)
    
    if 'model' in request.GET:
        model=request.GET['model']
        if model:
            all_cars=all_cars.filter(model__icontains=model)
    
    if 'year' in request.GET:
        year=request.GET['year']
        if year:
            all_cars=all_cars.filter(year__icontains=year)
    
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            all_cars=all_cars.filter(city__icontains=city)
    
    if 'body' in request.GET:
        body=request.GET['body']
        if body:
            all_cars=all_cars.filter(body_style__icontains=body)
    
    if 'transmission' in request.GET:
        transmission=request.GET['transmission']
        if transmission:
            all_cars=all_cars.filter(transmission__icontains=transmission)
    
    if 'min_price' in request.GET:
        min_price=request.GET['min_price']
        max_price=request.GET['max_price']
        if min_price:
            all_cars=all_cars.filter(price__gte=min_price,price__lte=max_price)
    
    
    data={'all_cars':all_cars,
        'make_fields':make_fields,
        'model_fields':model_fields,
        'year_fields':year_fields,
        'city_fields':city_fields,
        'body_fields':body_fields,    
        'transmission_fields':transmission_fields,    
    }
    
    return render(request,"cars/search.html",data)