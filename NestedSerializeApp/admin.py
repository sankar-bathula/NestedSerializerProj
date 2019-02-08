from django.contrib import admin
from NestedSerializeApp.models import Author, Book
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
	list_display = ['id', 'first_name', 'last_name', 'subject']

class BookAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'author', 'rating']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)