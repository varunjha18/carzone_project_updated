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