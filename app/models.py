from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.urls import reverse


class Artist(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse("artist:detail", kwargs={"id": self.id})


class Album(models.Model):
    artist = models.ForeignKey(Artist, related_name="album", on_delete=models.
                               CASCADE)
    name = models.CharField(max_length=100)
    release_Date = models.DateField()
    album_cover = models.ImageField(upload_to='Album')

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse("album:detail", kwargs={"id": self.id})


class Song(models.Model):
    song_Title = models.CharField(max_length=100, null=False, blank=False)
    album = models.ForeignKey(Album, related_name="song", on_delete=models.
                              CASCADE)
    artist = models.ForeignKey(Artist, related_name="song", on_delete=models.
                               CASCADE)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.song_Title


class Playlist(models.Model):
    playlist_Title = models.CharField(max_length=100)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    songs = models.ManyToManyField("Song")

    def __str__(self):
        return self.playlist_Title

    def get_url(self):
        return reverse("playlist:detail", kwargs={"id": self.id})
