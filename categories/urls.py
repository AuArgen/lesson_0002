from django.urls import path

from categories.views import index, details, bookdetails

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>',  details, name='details'),
    path('book/<int:book_id>',  bookdetails, name='details'),
]