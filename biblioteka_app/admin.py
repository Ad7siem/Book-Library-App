from django.contrib import admin
from .models import ListBook, ListPeople, ListBookCategory, ListPhoto, OpeningHours


# Registering Django models.
admin.site.register(ListBook)
admin.site.register(ListPeople)
admin.site.register(ListBookCategory)
admin.site.register(ListPhoto)
admin.site.register(OpeningHours)