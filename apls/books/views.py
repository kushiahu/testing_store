# Django
from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Models
from apls.books.models import Book


def book_index(request):
	books = Book.objects.all()
	ctx = {
		'books': books
	}
	return render(request, 'books/index_book.html', ctx)



def detail_view(request, slug):
	book = get_object_or_404(Book, slug=slug)
	return render(request, 'books/detail.html', {'book': book})