from django.contrib import admin

from apls.books.models import Author, Editorial, Book


admin.site.register(Author)
admin.site.register(Editorial)
admin.site.register(Book)