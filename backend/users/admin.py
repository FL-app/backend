from django.contrib import admin
from django.contrib.auth.models import Group

from users.models import CustomUser, FriendsRequest, FriendsRelationship, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Админка для тегов."""

    list_display = (
        "pk",
        "name",
        "color",
        "slug",
    )
    prepopulated_fields = {"slug": ["name"]}


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """Админка для юзеров."""

    list_display = (
        "pk",
        "username",
        "email",
        "status",
        "is_active",
    )

    def has_add_permission(self, request):
        return False


@admin.register(FriendsRequest)
class FriendsRequestAdmin(admin.ModelAdmin):
    """Админка запросов в друзья."""

    list_display = (
        "pk",
        "from_user",
        "to_user",
    )


@admin.register(FriendsRelationship)
class FriendsRelationshipAdmin(admin.ModelAdmin):
    """Админка для юзер-друзья."""

    list_display = (
        "pk",
        "current_user",
        "friend",
        "friend_category",
    )


admin.site.unregister(Group)
