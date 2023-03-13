from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from django.db.models import Q
from .models import ListBook, ListPeople, ListBookCategory
from .forms import ListBookForm, ListPeopleForm, ListBookCategoryForm
import csv, io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

from django.urls import reverse

# Create Home Page
def home(request):
    return render(request, 'home.html', {})

########################### USER ###########################
# Create Login
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Zalogowano!"))
            return redirect('home')
        else:
            messages.success(request, ("Złe hasło lub login. Spróbuj ponownie!"))
            return redirect('login')
    else:
        return render(request, 'login.html', {})

# Create Logout
def logout_user(request):
    logout(request)
    messages.success(request, ("Wylogowano!"))
    return redirect('home')

########################### BOOK LIST ###########################
# Show Book List
def book_list(request):
    books = ListBook.objects.all()
    return render(request, 'book_list.html', {'books': books})

# Show Admin Book List and Add, Edit, Deleted Buttons
def admin_book_list(request):
    admin_books = ListBook.objects.all()
    if request.method == "POST":
        form = ListBookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ("Książka została dodana do spisu"))
            return redirect('admin-books-list')
    else:
        form = ListBookForm

    return render(request, 'admin_books_list.html', 
                {
                    'books': admin_books, 
                    'form': form,
                })

# # Add Book to List  --------------------------------------------------------------------------------- Most likely, the book adding function will be removed.
# def add_book(request):
#     books = ListBook.objects.all()
#     if request.method == "POST":
#         form = ListBookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, ("Książka została dodana do spisu"))
#             return redirect('add-book')
#     else:
#         form = ListBookForm
#     return render(request, 'add_book.html', {'form': form, 'books': books })

# Update Book
def update_book(request, book_id):
    books = ListBook.objects.all()
    book_index = ListBook.objects.get(pk=book_id)
    form = ListBookForm(request.POST or None, instance=book_index)
    if form.is_valid():
        form.save()
        messages.success(request, ("Dane książki zostały zmienione"))
        return redirect('admin-books-list')
            
    return render(request, 'update_book.html', 
                {
                    'book_index':book_index,
                    'form':form,
                    'books':books,
                })
    # book_pk = get_object_or_404(ListBook, pk=book_id) -----------------------------------------------------------------Looking for a way to make the edit post function work in a "modal" style on the list page.
    # print("co kolwiek")
    # if request.method == "POST":
    #     form = ListBookForm(request.POST, instance=book_pk)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(reverse('admin-books-list'))
    # else:
    #     form = ListBookForm(instance=book_pk)
    # return render(request, 'update_book.html', { 'form': form, 'book_pk': book_pk, 'ck':ck,})

# Delete Book
def delete_book(request, book_id):
    book = ListBook.objects.get(pk=book_id)
    book.delete()
    messages.success(request, ("Książka została usunięta"))
    return redirect('admin-books-list')

########################### People List ###########################
# Show List People
def people_list(request):
    peoples = ListPeople.objects.all()
    if request.method == "POST":
        form = ListPeopleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ("Osoba została dodana do listy"))
            return redirect('peoples-list')
    else:
        form = ListPeopleForm
    return render(request, 'peoples_list.html', {'peoples':peoples, 'form': form, })

# # Add People to List ---------------------------------------------------------------- Most likely, the person adding function will be removed.
# def add_people(request):
#     peoples = ListPeople.objects.all()
#     if request.method == "POST":
#         form = ListPeopleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, ("Osoba została dodana do list"))
#             return redirect('add-people')
#     else:
#         form = ListPeopleForm
#     return render(request, 'add_people.html', {'form':form, 'peoples':peoples, })

# Update People
def update_people(request, people_id):
    peoples = ListPeople.objects.all()
    people_index = ListPeople.objects.get(pk=people_id)
    form = ListPeopleForm(request.POST or None, instance=people_index)
    if form.is_valid():
        form.save()
        messages.success(request, ("Dane osoby zostały zmienione"))
        return redirect('peoples-list')

    return render(request, 'update_people.html', 
                {
                    'people_index':people_index,
                    'form':form,
                    'peoples':peoples,
                }) 

# Delete People
def delete_people(request, people_id):
    people = ListPeople.objects.get(pk=people_id)
    people.delete()
    messages.success(request, ("Osoba została usunięta"))
    return redirect('peoples-list')

########################### Category Book List ###########################
# Show List Categories
def categories_list(request):
    categories = ListBookCategory.objects.all()
    if request.method == "POST":
        form = ListBookCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ("Kategoria Książki została dodana do listy"))
            return redirect('categories-list')
    else:
        form = ListBookCategoryForm
    return render(request, 'categories_list.html', {'categories': categories, 'form': form,})

# # Add Category Book to List --------------------------------------------------- Most likely, the category adding function will be removed.
# def add_category(request):
#     categories = ListBookCategory.objects.all()
#     if request.method == "POST":
#         form = ListBookCategoryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, ("Kategoria Książki została dodana do listy"))
#             return redirect('add-category')
#     else:
#         form = ListBookCategoryForm
#     return render(request, 'add_category.html', {'form': form, 'categories': categories, })

# Update Category
def update_category(request, category_id):
    categories = ListBookCategory.objects.all()
    category_index = ListBookCategory.objects.get(pk=category_id)
    form = ListBookCategoryForm(request.POST or None, instance=category_index)
    if form.is_valid():
        form.save()
        messages.success(request, ("Nazwa Kategorii została zmieniona"))
        return redirect('categories-list')
    
    return render(request, 'update_category.html',
                {
                    'category_index':category_index,
                    'form':form,
                    'categories':categories,
                })

# Delete Category
def delete_category(request, category_id):
    category = ListBookCategory.objects.get(pk=category_id)
    category.delete()
    messages.success(request, ("Kategoria została usunięta"))
    return redirect('categories-list')

########################### Search ###########################
# Searching for book titles or categories
def search_main(request):
    if request.method == "POST":
        searched = request.POST['searched']
        books = ListBook.objects.filter(Q(title__icontains=searched) | Q(category__name__icontains=searched)).distinct()
        return render(request, 'search_main.html',
                    {
                        'searched': searched,
                        'books': books,
                    })
    else:
        return redirect('book-list')
    
# Searching for book - Admin
def search_book_admin(request):
    if request.method == "POST":
        searched = request.POST['searched']
        books = ListBook.objects.filter(title__icontains=searched)
        return render(request, 'search_books_admin.html',
                    {
                        'searched': searched,
                        'books': books,
                    })
    else:
        return redirect('admin-books-list')

# Searching for people - Admin
def search_people_admin(request):
    if request.method == "POST":
        searched = request.POST['searched']
        peoples = ListPeople.objects.filter(Q(first_name__icontains=searched) | Q(last_name__icontains=searched))
        return render(request, 'search_peoples_admin.html',
                    {
                        'searched': searched,
                        'peoples': peoples,
                    })
    else:
        return redirect('people-list')
    
# Searching for category - Admin
def search_categories_admin(request):
    if request.method == "POST":
        searched = request.POST['searched']
        categories = ListBookCategory.objects.filter(name__icontains=searched)
        return render(request, 'search_categories_admin.html', 
                    {
                        'searched': searched,
                        'categories': categories,
                    })
    else:
        return redirect('categories-list')


########################### Download File ###########################
# Download PDF   ------------------------- Lack of Polish characters. / Brak polskich znaków.
def pdf_book(response):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Times-Roman", 14)
    
    lines = []
    books = ListBook.objects.all()

    for book in books:
        lines.append(book.title)
        lines.append(book.author)
        lines.append(book.location)
        lines.append(', '.join(book.category.all().values_list('name', flat=True)))
        lines.append(book.notes)
        lines.append("================================")

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='list_books.pdf')

# Download TXT
def txt_book(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=listbook.txt'

    books = ListBook.objects.all()
    lines = []
    for book in books:
        lines.append(f'Tytuł: {book.title}\nAutor: {book.author}\nMiejsce: {book.location}\nKategoria: {", ".join(book.category.all().values_list("name", flat=True))}\nUwagi: {book.notes}\n\n')
    response.writelines(lines)
    return response

# Download CSV  ---------------------------------------- The file saves everything in one column. It should save each title to a separate column. / Plik zapisuje wszystko w jednej kolumnie. Powinien zapisywać każdy tytuł do oddzielnej kolumny.
def csv_book(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=book.csv'

    writer = csv.writer(response, delimiter=',')

    books = ListBook.objects.all()

    writer.writerow(['Tytuł','Autor', 'Miejsce', 'Kategoria', 'Uwagi'])

    for book in books:
        writer.writerow([book.title, book.author, book.location, ", ".join(book.category.all().values_list('name', flat=True)), book.notes])


    return response