from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django.db.models import Count
from .serializers import FilmSerializer
from .models import FilmModel
from .utils.utils import fetchFilms

# Db sync endpoint
@api_view(["POST"])
def sync_films(request):
    fetchFilms()
    return Response({"msg":"Database successfully synced!"})

# GET all films endpoint
class FilmListView(ListAPIView):
    serializer_class = FilmSerializer

    def get_queryset(self):
        return FilmModel.objects.annotate(comment_count=Count("comments")).order_by("release_date")