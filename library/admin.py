from django.contrib import admin
from .models import User, Book, Track, Note
# Register your models here.

admin.site.register(User)
admin.site.register(Book)
admin.site.register(Track)
admin.site.register(Note)