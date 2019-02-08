from rest_framework import serializers
from NestedSerializeApp.models import Author, Book

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
	books_author = BookSerializer(read_only=True, many=True)
	class Meta:
		model = Author
		fields = '__all__'
