from django.shortcuts import render

from categories.models import Category, Book


# Create your views here.


def index(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'index.html', context)

def details(request, category_id):
    choose = Category.objects.get(id=category_id)
    categories = Category.objects.all()
    books = Book.objects.filter(category=category_id)
    context = {
        'choose': choose,
        'categories': categories,
        'books': books,
    }
    return render(request, 'details.html', context)

def bookdetails(request, book_id):
    book = Book.objects.get(id=book_id)
    books = Book.objects.filter(category=book.category)
    choose = Category.objects.get(id=book.category)
    categories = Category.objects.all()
    context = {
        'choose': choose,
        'books': books,
        'categories': categories,
        'book': book,
    }

    return render(request, 'bookdetails.html', context)