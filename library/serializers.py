from .models import User, Book, Note, Track
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id','title', 'author', 'publication_date', 'genre','featured') 

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username') 

class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ('id','user', 'created_at','updated_at','notes', 'private') 

class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Track
        fields = ('id','book', 'user', 'status') 
