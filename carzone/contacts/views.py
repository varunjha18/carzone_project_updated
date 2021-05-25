from django.contrib import messages,auth
from contacts.models import Contact
from django.shortcuts import redirect, render
from django.core.mail import send_mail

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

        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted=Contact.objects.all().filter(car_id=car_id,user_id=user_id)
            if has_contacted:
                messages.error(request,"you have already made an enquiry regardin this car")
                return redirect('/cars/'+car_id)

        send_mail('New inquiry','This is a test message to test django emailing',
        'varunjha1245@gmail.com',['varunjha2000@gmail.com'],fail_silently=False,)

        contact=Contact(first_name=first_name,last_name=last_name,car_id=car_id,user_id=user_id,car_title=car_title,customer_needs=customer_needs,city=city,state=state,email=email,phone=phone,message=message,)

        contact.save()
        messages.success(request,'You inquiry for this car has been registered')
        return redirect('/cars/'+car_id)
    return 0