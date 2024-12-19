from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/<int:book_id>/', views.book, name='book'),
]