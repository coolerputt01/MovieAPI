from django.urls import path
from .views import sync_films,FilmListView

urlpatterns = [
    path('films/',FilmListView.as_view(),name="film-list"),
    path('sync-films/',sync_films,name="sync-films"),
]