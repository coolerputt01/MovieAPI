from django.urls import path
from .views import CommentCreateView,CommentListView

urlpatterns = [
    path("film/<int:film_id>/comments/",CommentListView.as_view(),name="comment-list"),
    path("film/<int:film_id>/comments/create/", CommentCreateView.as_view(), name="comment-create"),
]