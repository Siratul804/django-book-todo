
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Book

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def book_list(request):
    if request.method == 'POST':
        Book.objects.create(
            user=request.user,
            title=request.POST.get('title')
        )
        return redirect('/')
    books = Book.objects.filter(user=request.user)
    return render(request, 'books/list.html', {'books': books})

@login_required
def toggle_book(request, pk):
    book = Book.objects.get(pk=pk, user=request.user)
    book.completed = not book.completed
    book.save()
    return redirect('/')

@login_required
def delete_book(request, pk):
    Book.objects.get(pk=pk, user=request.user).delete()
    return redirect('/')
