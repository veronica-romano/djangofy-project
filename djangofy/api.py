from rest_framework import routers
from app import api_views as app_views


router = routers.DefaultRouter()
router.register('artists', app_views.ArtistViewset)
router.register('albums', app_views.AlbumViewset)
router.register('songs', app_views.SongViewset)
router.register('playlists', app_views.PlaylistViewset)
