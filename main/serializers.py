from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    """book serializer. The validate function makes the title words follow the title format"""
    class Meta:
        model = Book
        fields = ['title','img','author','availability','borrowership','owner']

        def validate_title(self, content):
            lines = content.split(' ')
            for line in lines:
                if line[0].islower():
                    line[0].upper
            return
