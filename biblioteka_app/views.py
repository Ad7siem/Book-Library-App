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

from django.utils.encoding import smart_str
from django.core.paginator import Paginator

### Create Home Page
def home(request):
    return render(request, 'home.html', {})

########################### USER ###########################
### Create Login
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

### Create Logout
def logout_user(request):
    logout(request)
    messages.success(request, ("Wylogowano!"))
    return redirect('home')

########################### BOOK LIST ###########################
### Show Book List
def book_list(request):
    # Access to all books saved in the database.
    books = ListBook.objects.all()

    # Creating pagination from all books in the database.
    p = Paginator(books, 10)
    page = request.GET.get('page')
    list_book = p.get_page(page)
    nums = "a" * list_book.paginator.num_pages

    # Rendering a page with function variables.
    return render(request, 'book_list.html', 
                {
                    'books': books,
                    'list_book': list_book,
                    'nums': nums,
                })

### Show Admin Book List and Add, Deleted Buttons
def admin_book_list(request):
    # Access to all books saved in the database.
    admin_books = ListBook.objects.all()

    # Creating pagination from all books in the database.
    p = Paginator(admin_books, 10)
    page = request.GET.get('page')
    list_book = p.get_page(page)
    nums = "a" * list_book.paginator.num_pages

    # Creating a form object.
    if request.method == "POST":
        form = ListBookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ("Książka została dodana do spisu"))
            return redirect('admin-books-list')
    else:
        form = ListBookForm

    # Rendering a page with function variables.
    return render(request, 'admin_books_list.html', 
                {
                    'books': admin_books, 
                    'form': form,
                    'list_book': list_book,
                    'nums': nums,
                })

### Update Book
def update_book(request, book_id):
    # Accesz to all books saved in the database.
    books = ListBook.objects.all()

    # Creating pagination from all books in the database.
    p = Paginator(books, 8)
    page = request.GET.get('page')
    list_book = p.get_page(page)
    nums = "a" * list_book.paginator.num_pages

    # Creating a form for editing a book.
    book_index = ListBook.objects.get(pk=book_id)
    # form = ListBookForm(request.POST or None, instance=book_index)
    if request.method == "POST":
        form = ListBookForm(request.POST, instance=book_index)
        if form.is_valid():
            form.save()
            messages.success(request, ("Dane książki zostały zmienione"))
            return redirect('admin-books-list')
    else:
        form = ListBookForm(instance=book_index)

    # Rendering a page with function variables.   
    return render(request, 'update_book.html', 
                {
                    'book_index':book_index,
                    'form':form,
                    'books':books,
                    'list_book': list_book,
                    'nums': nums,
                })

### Delete Book
def delete_book(request, book_id):
    book = ListBook.objects.get(pk=book_id)
    book.delete()
    messages.success(request, ("Książka została usunięta"))
    return redirect('admin-books-list')

########################### People List ###########################
### Show List People
def people_list(request):
    # Access to all People saved in the database.
    peoples = ListPeople.objects.all()

    # Creating paginatrion from all people in the database.
    p = Paginator(peoples, 10)
    page = request.GET.get('page')
    list_peoples = p.get_page(page)
    nums = "a" * list_peoples.paginator.num_pages

    # Creating a form object
    if request.method == "POST":
        form = ListPeopleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ("Osoba została dodana do listy"))
            return redirect('peoples-list')
    else:
        form = ListPeopleForm

    # Rendering a page with function variables.
    return render(request, 'peoples_list.html', 
                {
                    'peoples':peoples, 
                    'form': form, 
                    'list_peoples': list_peoples,
                    'nums': nums,
                })

### Update People
def update_people(request, people_id):
    # Access to all peoples saved in the database.
    peoples = ListPeople.objects.all()

    # Creating pagination from all peoples in the database.
    p = Paginator(peoples, 8)
    page = request.GET.get('page')
    list_peoples = p.get_page(page)
    nums = "a" * list_peoples.paginator.num_pages

    # Creating a form for editing a people.
    people_index = ListPeople.objects.get(pk=people_id)
    if request.method == "POST":
        form = ListPeopleForm(request.POST, instance=people_index)
        if form.is_valid():
            form.save()
            messages.success(request, ("Dane osoby zostały zmienione"))
            return redirect('peoples-list')
    else:
        form = ListPeopleForm(instance=people_index)

    # Rendering a page with function variables.
    return render(request, 'update_people.html', 
                {
                    'people_index':people_index,
                    'form':form,
                    'peoples':peoples,
                    'list_peoples': list_peoples,
                    'nums': nums,
                }) 

### Delete People
def delete_people(request, people_id):
    people = ListPeople.objects.get(pk=people_id)
    people.delete()
    messages.success(request, ("Osoba została usunięta"))
    return redirect('peoples-list')

########################### Category Book List ###########################
### Show List Categories
def categories_list(request):
    # Access to all categories saved in the database.
    categories = ListBookCategory.objects.all()

    # Creating pagination from all categories in the database.
    p = Paginator(categories, 10)
    page = request.GET.get('page')
    list_categories = p.get_page(page)
    nums = "a" * list_categories.paginator.num_pages

    # Creating a form object.
    if request.method == "POST":
        form = ListBookCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ("Kategoria Książki została dodana do listy"))
            return redirect('categories-list')
    else:
        form = ListBookCategoryForm

    # Rendering a page with function variables.
    return render(request, 'categories_list.html', 
                {
                    'categories': categories, 
                    'form': form,
                    'list_categories': list_categories,
                    'nums': nums,
                })

### Update Category
def update_category(request, category_id):
    # Access to all categories saved in the database
    categories = ListBookCategory.objects.all()

    # Creating pagination from all categories in the database.
    p = Paginator(categories, 8)
    page = request.GET.get('page')
    list_categories = p.get_page(page)
    nums = "a" * list_categories.paginator.num_pages

    # Creating a form for editing a category
    category_index = ListBookCategory.objects.get(pk=category_id)
    if request.method == "POST":
        form = ListBookCategoryForm(request.POST, instance=category_index)
        if form.is_valid():
            form.save()
            messages.success(request, ("Nazwa Kategorii została zmieniona"))
            return redirect('categories-list')
    else:
        form = ListBookCategoryForm(instance=category_index)
    
    # Rendring a page with function variables.
    return render(request, 'update_category.html',
                {
                    'category_index':category_index,
                    'form':form,
                    'categories':categories,
                    'list_categories': list_categories,
                    'nums': nums,
                })

### Delete Category
def delete_category(request, category_id):
    category = ListBookCategory.objects.get(pk=category_id)
    category.delete()
    messages.success(request, ("Kategoria została usunięta"))
    return redirect('categories-list')

########################### Search ###########################
### Searching for book titles or categories
def search_main(request):
    #
    if request.method == "POST":
        searched = request.POST['searched']
        request.session['searched'] = searched
    else:
        searched = request.session.get('searched', '')

    books = ListBook.objects.filter(Q(title__icontains=searched) | Q(category__name__icontains=searched)).order_by('id').distinct()

    # Creating pagination from searched books in the database.
    p = Paginator(books, 10)
    page = request.GET.get('page')
    list_books = p.get_page(page)
    nums = "a" * list_books.paginator.num_pages

    # Rendering a page with function variables.
    return render(request, 'search_main.html',
                {
                    'searched': searched,
                    'books': list_books,
                    'list_books': list_books,
                    'nums': nums,
                })

    
### Searching for book - Admin
def search_book_admin(request):
    #
    if request.method == "POST":
        searched = request.POST['searched']
        request.session['searched'] = searched
    else:
        searched = request.session.get('searched', '')

    books = ListBook.objects.filter(title__icontains=searched)

    # Creating pagination from searched books in the database.
    p = Paginator(books, 10)
    page = request.GET.get('page')
    list_books = p.get_page(page) 
    nums = "a" * list_books.paginator.num_pages

    # Rendering a page with function variables.
    return render(request, 'search_books_admin.html',
                {
                    'searched': searched,
                    'books': books,
                    'list_books': list_books,
                    'nums': nums,
                })

### Searching for people - Admin
def search_people_admin(request):
    #
    if request.method == "POST":
        searched = request.POST['searched']
        request.session['searched'] = searched
    else:
        searched = request.session.get('searched', '')

    peoples = ListPeople.objects.filter(Q(first_name__icontains=searched) | Q(last_name__icontains=searched))

    # Creating pagination from searched peoples in the database.
    p = Paginator(peoples, 10)
    page = request.GET.get('page')
    list_peoples = p.get_page(page)
    nums = "a" * list_peoples.paginator.num_pages

    # Rendering a page with function variables.
    return render(request, 'search_peoples_admin.html',
                {
                    'searched': searched,
                    'peoples': peoples,
                    'list_peoples': list_peoples,
                    'nums': nums,
                })

    
### Searching for category - Admin
def search_categories_admin(request):
    #
    if request.method == "POST":
        searched = request.POST['searched']
        request.session['searched'] = searched
    else:
        searched = request.session.get('searched', '')

    categories = ListBookCategory.objects.filter(name__icontains=searched)

    # Creating pagination from searched category in the database.
    p = Paginator(categories, 10)
    page = request.GET.get('page')
    list_categories = p.get_page(page)
    nums = "a" * list_categories.paginator.num_pages

    # Rendering a page with function variables.
    return render(request, 'search_categories_admin.html', 
                {
                    'searched': searched,
                    'categories': categories,
                    'list_categories': list_categories,
                    'nums': nums,
                })


########################### Download File ###########################
### Download PDF   ------------------------- Lack of Polish characters. / Brak polskich znaków.
def pdf_book(response):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
    
    lines = []
    books = ListBook.objects.all()

    for book in books:
        lines.append(smart_str(book.title))
        lines.append(smart_str(book.author))
        lines.append(smart_str(book.location))
        lines.append(smart_str(', '.join(book.category.all().values_list('name', flat=True))))
        lines.append(smart_str(book.notes))
        lines.append("================================")

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='list_books.pdf')

### Download TXT
def txt_book(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=listbook.txt'

    books = ListBook.objects.all()
    lines = []
    for book in books:
        lines.append(f'Tytuł: {book.title}\nAutor: {book.author}\nMiejsce: {book.location}\nKategoria: {", ".join(book.category.all().values_list("name", flat=True))}\nUwagi: {book.notes}\n\n')
    response.writelines(lines)
    return response

### Download CSV  ---------------------------------------- Lack of Polish characters. / Brak polskich znaków.
def csv_book(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=book.csv'

    writer = csv.writer(response, delimiter=';')

    books = ListBook.objects.all()

    writer.writerow(['Tytuł','Autor', 'Miejsce', 'Kategoria', 'Uwagi'])

    for book in books:
        writer.writerow([book.title, book.author, book.location, ", ".join(book.category.all().values_list('name', flat=True)), book.notes])


    return response