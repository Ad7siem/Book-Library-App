from django import forms
from django.forms import ModelForm
from .models import ListBook, ListPeople, ListBookCategory


# Create a List Book Form
class ListBookForm(ModelForm):
    class Meta:
        model = ListBook
        fields = ('title', 'author', 'location', 'category', 'borrow_date', 'borrower', 'notes')
        labels = {
            'title':'', 
            'author':'', 
            'location':'', 
            'category':'', 
            'borrow_date':'', 
            'borrower':'', 
            'notes':'',
        }
        widgets={
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nazwa książki'}), 
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Autor książki'}), 
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lokacja książki'}), 
            'category': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Kategorie'}), 
            'borrow_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), 
            'borrower': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Osoba wypożyczająca'}), 
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Uwagi'}),
        }

# Create a List People Form
class ListPeopleForm(ModelForm):
    class Meta:
        model = ListPeople
        fields = ('first_name', 'last_name', 'note', 'contact')
        labels = {
            'first_name':'',
            'last_name':'',
            'note':'',
            'contact':'',
        }
        widgets={
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Imię'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nazwisko'}),
            'note':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Uwagi'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Kontakt'}),
        }

# Create a List Book Category Form
class ListBookCategoryForm(ModelForm):
    class Meta:
        model = ListBookCategory
        fields = {'name',}
        labels = {
            'name':'',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nazwa'})
        }