from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

app_name = "app"

urlpatterns = [
    path("view/artists", views.ArtistListView.as_view(), name="ArtistList"),
    path("view/artist/<int:pk>",
         views.ArtistDetailView.as_view(), name="ArtistDetail"),
    path("view/albums", views.AlbumListView.as_view(), name="AlbumList"),
    path("view/songs", views.SongListView.as_view(), name="SongList"),
    path("view/playlists",
         views.PlaylistListView.as_view(), name="PlaylistList"),
    path("view/album/<int:pk>",
         views.AlbumDetailView.as_view(), name="AlbumDetail"),
    path("view/playlist/<int:pk>",
         views.PlaylistDetailView.as_view(), name="PlaylistDetail"),
    path("", views.index.as_view(), name="Index")

]
