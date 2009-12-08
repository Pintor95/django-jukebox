from django.conf.urls.defaults import *

urlpatterns = patterns('apps.music_player.views',
    url(r'^$', 'music_player_main', 
        name='music_player_main'),
    url(r'^song_queue/$', 'display_song_queue', 
        name='music_player-display_song_queue'),
    url(r'^song_search/$', 'song_search', 
        name='music_player-song_search'),
    url(r'^song_search_results/$', 'song_search_results', 
        name='music_player-song_search_results'),
    url(r'^request_song/(?P<song_id>\d+)/$', 'request_song', 
        name='music_player-request_song'),   
)