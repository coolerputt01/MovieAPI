from rest_framework import serializers
from .models import CommentModel

# Film Comment Serializer.
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = [
            "id","film_id","content","created_at"
        ]
        read_only_fields = ["id", "created_at"]
