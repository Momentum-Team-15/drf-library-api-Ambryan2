"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from library import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('registration.backends.simple.urls')),
    path('books/', views.BookList.as_view(), name='book_list'),
    path('books/<int:pk>',views.BookDetail.as_view(), name='book_detail'),
    path('tracking/',views.TrackList.as_view(), name='track_list'),
    path('tracking/<int:pk>',views.TrackDetail.as_view(), name='track_detail'),
    path('notes/', views.NotesList.as_view(), name='notes_list'),
    path('notes/<int:pk>',views.NoteDetail.as_view(), name='note_detail'),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
