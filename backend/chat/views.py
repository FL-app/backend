from rest_framework import viewsets
from drf_spectacular.utils import extend_schema

from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer


@extend_schema(
    tags=['message_room'],
)
class RoomViewSet(viewsets.ModelViewSet):
    """CRUD для комнаты."""

    queryset = Room.objects.all()
    serializer_class = RoomSerializer


@extend_schema(
    tags=['message'],
)
class MessageViewSet(viewsets.ModelViewSet):
    """CRUD для сообщений."""

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
