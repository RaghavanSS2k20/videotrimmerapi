from django.urls import path
from .views import videoList, video,addVideo, trimVideo
urlpatterns = [
    path('videos/', videoList, name = "videoList"),
    path('get/<int:video_id>/', video, name="vidoById"),
    path('upload/', addVideo, name='addVideo'),
    path('trim/<int:video_id>/', trimVideo, name='trimVideo'),
]