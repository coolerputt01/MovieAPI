from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.exceptions import NotFound
from films.models import FilmModel
from .models import CommentModel
from .serializers import CommentSerializer
from .pagination import CommentPagination

from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter,
    OpenApiResponse,
)

# ===========================
# CREATE COMMENT
# ===========================
@extend_schema(
    summary="Create a comment for a film",
    description="Creates a new comment attached to a specific film",
    parameters=[
        OpenApiParameter(
            name="film_id",
            type=int,
            location=OpenApiParameter.PATH,
            description="ID of the film",
        )
    ],
    request=CommentSerializer,
    responses={
        201: CommentSerializer,
        404: OpenApiResponse(description="Film not found"),
    },
    tags=["Comments"],
)
class CommentCreateView(CreateAPIView):
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        film_id = self.kwargs.get("film_id")

        try:
            film = FilmModel.objects.get(id=film_id)
        except FilmModel.DoesNotExist:
            raise NotFound("Film not found!")

        serializer.save(film=film)


# ===========================
# LIST COMMENTS (NO PAGINATION)
# ===========================
@extend_schema(
    summary="List comments for a film",
    description="Returns all comments for a film ordered by creation date",
    parameters=[
        OpenApiParameter(
            name="film_id",
            type=int,
            location=OpenApiParameter.PATH,
            description="ID of the film",
        )
    ],
    responses={200: CommentSerializer(many=True)},
    tags=["Comments"],
)
class CommentListView(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        film_id = self.kwargs.get("film_id")
        return CommentModel.objects.filter(
            film_id=film_id
        ).order_by("created_at")


# ===========================
# LIST COMMENTS (PAGINATED)
# ===========================
@extend_schema(
    summary="List comments for a film (paginated)",
    description="Returns paginated comments ordered by newest first",
    parameters=[
        OpenApiParameter(
            name="film_id",
            type=int,
            location=OpenApiParameter.PATH,
            description="ID of the film",
        )
    ],
    responses={200: CommentSerializer(many=True)},
    tags=["Comments"],
)
class CommentPaginatedListView(ListAPIView):
    serializer_class = CommentSerializer
    pagination_class = CommentPagination

    def get_queryset(self):
        film_id = self.kwargs.get("film_id")
        return CommentModel.objects.filter(
            film_id=film_id
        ).order_by("-created_at")
