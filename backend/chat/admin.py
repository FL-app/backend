from django.contrib import admin

from .models import Room


@admin.register(Room)
class CustomUserAdmin(admin.ModelAdmin):
    """Админка для чата."""

    list_display = (
        "room",
        "user",
        "text",
    )
