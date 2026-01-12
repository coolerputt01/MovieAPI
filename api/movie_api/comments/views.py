from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.exceptions import NotFound
from films.models import FilmModel
from .models import CommentModel
from .serializers import CommentSerializer

# CREATE a comment for a Film.
class CommentCreateView(CreateAPIView):
    serializer_class = CommentSerializer

    def perform_create(self,serializer):
        film_id = self.kwargs.get("film_id")
        try:
            film = FilmModel.objects.get(id=film_id)
        except FilmModel.DoesNotExist:
            raise NotFound("Film not found!")

        serializer.save(film_id=film)

# GET all comments from a Film.
class CommentListView(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        film_id = self.kwargs.get("film_id")
        return CommentModel.objects.filter(film_id=film_id).order_by("created_at")
