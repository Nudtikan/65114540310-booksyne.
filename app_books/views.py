from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def books(request):
    return HttpResponse('BookNest')

def book(request, book_id):
    return HttpResponse(f"Book ID: {book_id}")

def book(request, book_id):
    return HttpResponse('Book ID = ' + str(book_id))