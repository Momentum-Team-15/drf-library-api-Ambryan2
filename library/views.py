from rest_framework import generics, permissions, renderers
from rest_framework.views import APIView
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework.reverse import reverse
from django.http import Http404
from rest_framework import status

from .models import Book,User,Track,Note
from .permissions import IsOwnerOrReadOnly
from .serializers import BookSerializer, UserSerializer, NoteSerializer, TrackSerializer

# Just need to add permissions

# TODO Api_view so that we can go between views
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'tracks': reverse('track_list', request=request, format=format),
        'books': reverse('book_list', request=request, format=format),
        'notes': reverse('notes_list', request=request, format=format),
    })

#TODO view for all books, create book, to view all featured books
class BookList(APIView):
    books = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

    def get(self, request, format=None):
        """
        Return a list of all books.
        """
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Add a book to all books
        """
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Edit book and delete book. Still Not finished
class BookDetail(APIView):
    books = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

    def get(self, request,pk, format=None):
        """
        Return a list of all books.
        """
        books = Book.objects.filter(id=pk)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        """
        Allow user to update a book being tracked. Note that only admins should be allowed to perform this action
        """
        book = Book.objects.filter(id=pk)
        serializer = BookSerializer(book, data=request.data)
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        """
        Note that only admins should be able to perform this action
        """
        book = Book.objects.get(id=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# TODO track that allows users to create a book to track, displays all tracked, and allow to update
class TrackList(APIView):
    def get(self, request, format=None):
        """
        Return a list of all tracks.
        Note That only the user tracking should be able to see
        """
        tracked = Track.objects.all()
        serializer = TrackSerializer(tracked, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        """
        Allow user to tack a book.
        Note that only the user should be able to perform action
        """
        serializer = TrackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,id,format=None):
        """
        Allow user to update a book being tracked
        Note that only user should be able to update
        """
        track = self.get_object(id)
        serializer = TrackSerializer(track, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Need a track detail so indiv can update tracks


# TODO view to edit note, read all notes, and create note 
class NotesList(APIView):
    def get(self, request, format=None):
        """
        Return a list of all Notes.
        Note only the user should see their notes. Unless a note is shown as public
        """
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        """
        Allow user to make a note on a book.
        Only user should be able to make a new note on a book
        """
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,id,format=None):
        """
        Allow user to update a note on a book.
        Only user can update their note on a book
        """
        note = self.get_object(id)
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# need a notes detail so indiv can edit said field 