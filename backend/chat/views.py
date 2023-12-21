from rest_framework import viewsets

from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer


class RoomViewSet(viewsets.ModelViewSet):
    """CRUD для комнаты."""

    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class MessageViewSet(viewsets.ModelViewSet):
    """CRUD для сообщений."""

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
