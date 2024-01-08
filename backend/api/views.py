from rest_framework.viewsets import ReadOnlyModelViewSet
from drf_spectacular.utils import extend_schema

from users.models import Tag

from .serializers import TagSerializer


@extend_schema(
    tags=['tags'],
)
class TagViewSet(ReadOnlyModelViewSet):
    """Вьюсет для модели Тегов."""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None
