from rest_framework import viewsets
from . import models, serializers


class ArtistViewset(viewsets.ModelViewSet):
    queryset = models.Artist.objects.all()
    serializer_class = serializers.ArtistSerializer


class AlbumViewset(viewsets.ModelViewSet):
    queryset = models.Album.objects.all()
    serializer_class = serializers.AlbumSerializer


class SongViewset(viewsets.ModelViewSet):
    queryset = models.Song.objects.all()
    serializer_class = serializers.SongSerializer


class PlaylistViewset(viewsets.ModelViewSet):
    queryset = models.Playlist.objects.all()
    serializer_class = serializers.PlaylistSerializer
