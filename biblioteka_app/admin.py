from django.contrib import admin
from .models import ListBook, ListPeople, ListBookCategory


# Registering Django models.
admin.site.register(ListBook)
admin.site.register(ListPeople)
admin.site.register(ListBookCategory)
