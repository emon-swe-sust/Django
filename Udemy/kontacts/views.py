from django.shortcuts import render,redirect 
from django.contrib import messages
from .models import Kontact

# Create your views here.
def kontact(request):
    if request.method == 'POST':
        print('HEllo')
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        kontact = Kontact(listing=listing, listing_id=listing_id, name= name,
        email=email, phone=phone, user_id=user_id)

        kontact.save()

        messages.success(request, 'Your request is submitted')
        return redirect('/listings/'+listing_id)