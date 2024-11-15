from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

# View for listing all books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

# View for creating a new book
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the book list after saving
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

# View for updating an existing book
def book_update(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            # Redirect to the book list after updating
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form})

# View for confirming and deleting a book
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        # Redirect to the book list after deletion
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})
