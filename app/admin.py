from django.contrib import admin

from .models import Artist
from .models import Album
from .models import Song
from .models import Playlist

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("name", "genre")

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("artist", "name", "release_Date")

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("song_Title", "album", "artist", "genre")

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ("playlist_Title", "creator")
