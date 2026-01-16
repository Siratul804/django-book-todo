
from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('register/', views.register, name='register'),
    path('toggle/<int:pk>/', views.toggle_book),
    path('delete/<int:pk>/', views.delete_book),
]
