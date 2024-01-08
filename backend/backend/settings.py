import os
from datetime import timedelta
from pathlib import Path

from corsheaders.defaults import default_headers
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    default="django-insecure-hnx2%flrjxay-o@nh3#b+b+$c8zfavmnl629_250*y!xudtwn3",
)


DEBUG = True

ALLOWED_HOSTS = (
    os.getenv("LOCALHOST"),
    os.getenv("LOCALHOST_IP"),
    os.getenv("CONTAINER_NAME"),
    os.getenv("DOMAIN"),
    os.getenv("SERVER_IP"),
    os.getenv("EVERYONE"),
)


INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Сторонние либы
    "rest_framework",
    "rest_framework.authtoken",
    "djoser",
    "rest_framework_simplejwt",
    "colorfield",
    "django_filters",
    "drf_yasg",
    "corsheaders",
    "drf_spectacular",

    # Приложения
    "users.apps.UsersConfig",
    "api.apps.ApiConfig",
    "places.apps.PlacesConfig",
    "chat.apps.ChatConfig"
)

MIDDLEWARE = (
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

DOMAIN = os.getenv("DOMAIN")

# Убрать в проде
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://91.186.197.174",
    "http://" + DOMAIN,
    "https://" + DOMAIN,
    "null",
)

CORS_ALLOW_HEADERS = default_headers + ("Access-Control-Allow-Origin",)


ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"
ASGI_APPLICATION = "backend.asgi.application"

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [{'0.0.0.0', 8080}]
        }
    }
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#         "ATOMIC_REQUESTS": True,
#     }
# }

# Postgress
DATABASES = {
    "default": {
        "ENGINE": os.getenv(
            "DB_ENGINE", default="django.db.backends.postgresql"
        ),
        "NAME": os.getenv("DB_NAME", default="postgres"),
        "USER": os.getenv("POSTGRES_USER", default="postgres"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", default="adm"),
        "HOST": os.getenv("DB_HOST", default="db"),
        "PORT": os.getenv("DB_PORT", default="5432"),
        "ATOMIC_REQUESTS": True,
    }
}

AUTH_PASSWORD_VALIDATORS = (
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
    {
        "NAME": "users.validators.MaximumLengthValidator",
    },
)

NAME_REGEX_PATTERN = r"[А-Яа-яA-Za-z ]+"

LANGUAGE_CODE = "ru"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_TZ = True


STATIC_URL = "backend_static/"
STATIC_ROOT = BASE_DIR / "backend_static"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


REST_FRAMEWORK = {
    "DEFAULT_THROTTLE_CLASSES": (
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle"
    ),
    "DEFAULT_THROTTLE_RATES": {
        "anon": "120/min",
        "user": "120/min",
    },
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SITE_NAME = DOMAIN

# Чтобы POST/PATCH можно было без слэша в конце юзать
# APPEND_SLASH = False

DJOSER = {
    "HIDE_USERS": False,
    "LOGIN_FIELD": "email",
    "SERIALIZERS": {
        "user_create": "users.serializers.CustomUserCreateSerializer",
        "user": "users.serializers.CustomUserSerializer",
        "current_user": "users.serializers.CustomUserSerializer",
    },
    "ACTIVATION_URL": os.getenv("ACTIVATION_URL",
                                default="#/activate/{uid}/{token}/"),
    # ACTIVATION_URL задается фронтом
    "SEND_ACTIVATION_EMAIL": True,

    # Это нужно будет согласовывать с фронтом: они должны будут принять эту
    # ссылку и вывести экран для ввода нового пароля, который вместе с uid и
    # token улетит на password_reset_confirm
    # "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    # "PASSWORD_RESET_CONFIRM_URL": "api/password-change/{uid}/{token}",
    # "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "AUTH_HEADER_TYPES": ("Bearer",),
}

INTERNAL_IPS = (
    os.getenv("LOCALHOSTIP"),
)

CSRF_TRUSTED_ORIGINS = (
    "http://" + DOMAIN,
    "https://" + DOMAIN,
    "http://127.0.0.1",
    "http://91.186.197.174",
)
AUTH_USER_MODEL = "users.CustomUser"


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# For debugging, you can use this setting to send messages to the console:
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DJANGO_CHANNELS_REST_API = {}


SPECTACULAR_SETTINGS = {
    'TITLE': '"Where are my friends?" API',
    'DESCRIPTION': 'Specification for the backend project application '
                   '"Where are my friends?"',
    'VERSION': 'v1',
    'SERVE_INCLUDE_SCHEMA': False,
    'SWAGGER_UI_SETTINGS': {
        "filter": True,  # включить поиск по тегам
    },
    # 'COMPONENT_SPLIT_REQUEST': True
}
