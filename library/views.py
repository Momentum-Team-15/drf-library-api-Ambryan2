from rest_framework import generics, permissions, renderers
from rest_framework.views import APIView
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework.reverse import reverse
from django.http import Http404
from rest_framework import status
from django.db.models import Q
# from django.contrib.auth.decorators import login_required

from .models import Book,User,Track,Note
from .permissions import IsAdminOrReadOnly
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
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        """
        Return a list of all books.
        """
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True,context={'request': request})
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
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request,pk, format=None):
        """
        Return a list of all books.
        """
        books = Book.objects.filter(id=pk)
        serializer = BookSerializer(books, many=True,context={'request': request})
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        """
        Allow user to update a book being tracked. Note that only admins should be allowed to perform this action
        """
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
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
    tracks = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsAdminOrReadOnly,)


    def get(self, request, format=None):
        """
        Return a list of all tracks.
        Note That only the user tracking should be able to see
        """
        tracked = Track.objects.filter(user=request.user)
        serializer = TrackSerializer(tracked, many=True,context={'request': request})
        return Response(serializer.data)

    def post(self,request,format=None):
        """
        Allow user to tack a book.
        Note that only the user should be able to perform action
        """
        serializer = TrackSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Allow to look indiv track and be able to update tracks
class TrackDetail(APIView):
    tracks = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsAdminOrReadOnly,)
    # Note need to change to isOwner

    def get(self, request,pk, format=None):
        """
        Return a list of all tracks.
        """
        tracks = Track.objects.filter(id=pk)
        serializer = TrackSerializer(tracks, many=True,context={'request': request})
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        """
        Allow user to update a tracking status on a book. Note that only owner should be allowed to perform this action
        """
        track = Track.objects.get(id=pk)
        serializer = TrackSerializer(track, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)

# TODO view to edit note, read all notes, and create note 
class NotesList(APIView):
    notes = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsAdminOrReadOnly,)


    def get(self, request, format=None):
        """
        Return a list of all Notes.
        Note only the user should see their notes. Unless a note is shown as public
        """
        notes = Note.objects.filter(Q(private='Public') | Q(user=request.user))
        serializer = NoteSerializer(notes, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self,request,format=None):
        """
        Allow user to make a note on a book.
        Only user should be able to make a new note on a book
        """
        serializer = NoteSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# notes detail so indiv can edit indiv notes 
class NoteDetail(APIView):

    notes = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (permissions.IsAuthenticated,IsAdminOrReadOnly,)
    # Note need to change to isOwner

    def get(self, request,pk, format=None):
        """
        Return singular note.
        """
        note = Note.objects.filter(id=pk)
        serializer = NoteSerializer(note, many=True, context={'request': request})
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        """
        Allow user to update a note on a book. Note that only owner should be allowed to perform this action
        """
        note = Note.objects.get(id=pk)
        serializer = NoteSerializer(note, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)

# TODO write the above classes except using generics for practice