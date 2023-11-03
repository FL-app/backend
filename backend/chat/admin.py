from django.contrib import admin

from .models import Room, Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Админка для чата."""

    list_display = (
        "room",
        "user",
        "text",
    )
