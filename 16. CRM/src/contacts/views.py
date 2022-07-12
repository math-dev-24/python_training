from django.shortcuts import render, redirect
from API.crm import get_all_users, User


# Create your views here.
def index(request):
    return render(request, 'contacts/index.html', {'users': get_all_users()})


def page_add_contact(request):
    return render(request, "contacts/add.html")


def add_contact(request):
    last_name = request.POST.get("last_name")
    first_name = request.POST.get('first_name')
    address = request.POST.get('address')
    phone_number = request.POST.get('phone_number')
    user = User(first_name= first_name, last_name=last_name, address=address, phone_number=phone_number)
    user.save()

    return redirect('index')


def delete_contact(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')

    user = User(first_name=first_name, last_name=last_name)
    user.delete()
    return redirect('index')