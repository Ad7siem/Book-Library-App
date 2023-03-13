from django.db import models


class ListBookCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ListPeople(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    note = models.CharField(max_length=200, null=True, blank=True)
    contact = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class ListBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    category = models.ManyToManyField(ListBookCategory)
    borrow_date = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(ListPeople, on_delete=models.SET_NULL, max_length=100, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
    

    

