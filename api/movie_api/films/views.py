from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django.db.models import Count
from drf_spectacular.utils import extend_schema, OpenApiResponse
from .serializers import FilmSerializer
from .models import FilmModel
from .utils.utils import fetchFilms

# ===========================
# DB SYNC ENDPOINT
# ===========================
@extend_schema(
    summary="Sync films from external API",
    description="Fetch films from SWAPI or external source and store in the database.",
    responses={200: OpenApiResponse(description="Database successfully synced")},
    tags=["Films"],
)
@api_view(["POST"])
def sync_films(request):
    fetchFilms()
    return Response({"msg": "Database successfully synced!"})

# ===========================
# LIST FILMS
# ===========================
@extend_schema(
    summary="List all films",
    description="Returns all films ordered by release date with comment count.",
    responses={200: FilmSerializer(many=True)},
    tags=["Films"],
)
class FilmListView(ListAPIView):
    serializer_class = FilmSerializer

    def get_queryset(self):
        return (
            FilmModel.objects.annotate(comment_count=Count("comments"))
            .order_by("release_date")
        )
