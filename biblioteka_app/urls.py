from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('book_list/', views.book_list, name='book-list'),
    path('peoples_list/', views.people_list, name='peoples-list'),
    path('categories_list/', views.categories_list, name='categories-list'),
    # path('add_book/', views.add_book, name='add-book'),
    # path('add_people/', views.add_people, name='add-people'),
    # path('add_category/', views.add_category, name='add-category'),
    path('admin_book_list/', views.admin_book_list, name='admin-books-list'),
    path('update_book/<book_id>', views.update_book, name='update-book'),
    path('update_people/<people_id>', views.update_people, name='update-people'),
    path('update_category/<category_id>', views.update_category, name='update-category'),
    path('delete_book/<book_id>', views.delete_book, name='delete-book'),
    path('delete_people/<people_id>', views.delete_people, name='delete-people'),
    path('delete_category/<category_id>', views.delete_category, name='delete-category'),
    path('books_text', views.txt_book, name='books-text'),
    path('books_csv', views.csv_book, name='books-csv'),
    path('books_pdf', views.pdf_book, name='books-pdf'),
    path('search_main/', views.search_main, name='search-main'),
    path('search_books_admin/', views.search_book_admin, name='search-book-admin'),
    path('search_peoples_admin/', views.search_people_admin, name='search-peoples-admin'),
    path('search_categories_admin/', views.search_categories_admin, name="search-categories-admin"),
    path('user_web/', views.user_web, name='user-web'),
    path('set_image/', views.set_image, name='set-image'),
    # path('add_image/', views.add_image, name='add-image'),
    path('delete_image/', views.delete_image, name='delete-image'),
    path('set_quote/', views.set_quote, name='set-quote'),
    path('set_info_web/', views.set_info_web, name="set-info-web"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
