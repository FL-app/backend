from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LoginView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls", namespace="api")),
    # path("users/", include("users.urls", namespace="users")),
    path("social/", include("social_django.urls", namespace="social")),
    path('login/',
         LoginView.as_view(template_name='users/login.html'),
         name='login'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
