from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView
from .models import Artist, Album, Song, Playlist
from rest_framework import generics
from .serializers import ArtistSerializer, AlbumSerializer
from .serializers import SongSerializer, PlaylistSerializer


class index (TemplateView):
    template_name = "app/index.html"


class ArtistListView(ListView):
    model = Artist


class ArtistDetailView(DetailView):
    model = Artist


class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumListView(ListView):
    model = Album


class AlbumDetailView(DetailView):
    model = Album


class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SongListView(ListView):
    model = Song


class SongDetailView(DetailView):
    model = Song


class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class PlaylistListView(ListView):
    model = Playlist


class PlaylistDetailView(DetailView):
    model = Playlist


class PlaylistList(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
