from contacts.models import Contact
from django.shortcuts import redirect, render

# Create your views here.
def inquiry(request):
    if request.method== "POST":
        car_id=request.POST['car_id']
        user_id=request.POST['user_id']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        car_title=request.POST['car_title']
        customer_needs=request.POST['customer_need']
        city=request.POST['city']
        state=request.POST['state']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']

        contact=Contact(first_name=first_name,last_name=last_name,car_id=car_id,user_id=user_id,car_title=car_title,customer_needs=customer_needs,city=city,state=state,email=email,phone=phone,message=message,)

        contact.save()
        return redirect('/cars/'+car_id)
    return 0