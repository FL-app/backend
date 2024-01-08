from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import Place, SharedPlaces
from .permissions import IsAuthor
from .serializers import PlacesSerializer, SharingSerializer


class PlacesViewSet(viewsets.ModelViewSet):
    """CRUD для пользовательских мест."""

    queryset = Place.objects.all()
    serializer_class = PlacesSerializer
    permission_classes = (IsAuthor,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @extend_schema(
        summary='Поделиться локацией',
        description=' ',
        tags=['places'],
        parameters=[
            OpenApiParameter(
                name='id',
                location=OpenApiParameter.PATH,
                description='id локации',
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name='user_id',
                location=OpenApiParameter.PATH,
                description='id пользователя, которому отправляем локацию',
                required=True,
                type=str,
            )
        ],
    )
    @action(
        methods=["post"],
        detail=True,
        url_path="share-place",
    )
    def share_place(self, request, **kwargs):
        sharing_place = self.kwargs.get("pk")
        sharing_to_user = request.data.get("sharing_to_user")
        data = {
            "sharing_place": sharing_place,
            "sharing_to_user": sharing_to_user,
        }
        serializer = SharingSerializer(data=data, context={"request": request})

        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save(sharing_user=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(
        summary='Перестать делиться локацией',
        description=' ',
        # request=FriendSerializer,
        # responses=FriendSerializer,
        tags=['places'],
        parameters=[
            OpenApiParameter(
                name='id',
                location=OpenApiParameter.PATH,
                description='id локации',
                required=True,
                type=int,
            ),
            OpenApiParameter(
                name='user_id',
                location=OpenApiParameter.PATH,
                description='id пользователя, которому отправляем локацию',
                required=True,
                type=str,
            )
        ],
    )
    @action(
        methods=["delete"],
        detail=True,
        url_path="stop-sharing-place",
    )
    def stop_sharing_place(self, request, **kwargs):
        sharing_place = self.kwargs.get("pk")
        sharing_to_user = request.data.get("sharing_to_user")

        place = SharedPlaces.objects.filter(
            sharing_place=sharing_place,
            sharing_to_user=sharing_to_user,
            sharing_user=self.request.user,
        )

        if not place.exists():
            return Response(
                {"errors": "Такое место не шарится этому человеку."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        place.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema(
        summary='Все расшаренные локации',
        description=' ',
        # request=FriendSerializer,
        # responses=FriendSerializer,
        tags=['places'],
        parameters=[
            OpenApiParameter(
                name='user_id',
                location=OpenApiParameter.PATH,
                description='id пользователя, которому отправляем локацию',
                required=True,
                type=str,
            )
        ],
    )
    @action(
        methods=["get"],
        detail=False,
        url_path="all-shared-places",
    )
    def all_shared_places(self, request, user_id):
        all_requests = SharedPlaces.objects.filter(
            sharing_user=self.request.user
        )
        serializer = SharingSerializer(
            all_requests, many=True, context={"request": request}
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
