
from django.urls import path
from contacts.views import index, add_contact, delete_contact ,page_add_contact


urlpatterns = [
    path('', index, name="index"),
    path('ajouter/', page_add_contact , name="page-ajouter"),
    path('add/', add_contact, name="add-contact"),
    path('delete/', delete_contact , name="delete-contact")

]
