import os
from datetime import timedelta
from pathlib import Path

# import oauth2_provider.contrib.rest_framework
# import rest_framework_social_oauth2.backends
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
    "colorfield",
    "django_filters",
    "drf_yasg",
    "corsheaders",
    "elasticemailbackend",
    "social_django",
    "rest_framework_simplejwt",
    "rest_framework_social_oauth2",
    "oauth2_provider",

    # Приложения
    "users.apps.UsersConfig",
    "api.apps.ApiConfig",
    "places.apps.PlacesConfig",
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
    "social_django.middleware.SocialAuthExceptionMiddleware",
)

# Убрать в проде
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "null",
)

CORS_ALLOW_HEADERS = default_headers + ("Access-Control-Allow-Origin",)


ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # 'DIRS': [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        "ATOMIC_REQUESTS": True,
    }
}


# Postgress
# DATABASES = {
#     "default": {
#         "ENGINE": os.getenv("DB_ENGINE", default="django.db.backends.postgresql"),
#         "NAME": os.getenv("DB_NAME", default="postgres"),
#         "USER": os.getenv("POSTGRES_USER", default="postgres"),
#         "PASSWORD": os.getenv("POSTGRES_PASSWORD", default="adm"),
#         "HOST": os.getenv("DB_HOST", default="db"),
#         "PORT": os.getenv("DB_PORT", default="5432"),
#         "ATOMIC_REQUESTS": True,
#     }
# }


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
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
        "rest_framework_social_oauth2.authentication.SocialAuthentication",
    ),
}

DOMAIN = os.getenv("DOMAIN", default='')
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
    "ACTIVATION_URL": "api/account-activate/{uid}/{token}/",
    # "TOKEN_MODEL": None, # In case if only stateless tokens (e.g. JWT) are used in project it should be set to None.
    # "SEND_ACTIVATION_EMAIL": True,
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
)
AUTH_USER_MODEL = "users.CustomUser"

EMAIL_BACKEND = "elasticemailbackend.backend.ElasticEmailBackend"

ELASTICEMAIL_API_KEY = os.getenv("ELASTICEMAIL_API_KEY")
EMAIL_HOST_USER = os.getenv(
    "EMAIL_HOST_USER", default="friends-locator@yandex.ru"
)

EMAIL_SERVER = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_ADMIN = EMAIL_HOST_USER

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# SOCIAL_AUTH_FIELDS_STORED_IN_SESSION = ['local_password',]

SOCIAL_AUTH_JSONFIELD_CUSTOM = 'django.db.models.JSONField'
SOCIAL_AUTH_JSONFIELD_ENABLED = True

LOGIN_REDIRECT_URL = '/api/v1/users/me/'  # для отладки

AUTHENTICATION_BACKENDS = (
    "social_core.backends.vk.VKOAuth2",
    "social_core.backends.google.GoogleOAuth2",
    # "social_auth.backends.google.GoogleOAuth2Backend",
    # 'social_auth.backends.contrib.yandex.YandexOAuth2Backend',
    # 'social_auth.backends.contrib.odnoklassniki.OdnoklassnikiBackend',
    # "rest_framework_social_oauth2.backends.DjangoOAuth2",
    "django.contrib.auth.backends.ModelBackend",
)

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)


SOCIAL_AUTH_URL_NAMESPACE = 'social'

SOCIAL_AUTH_VK_OAUTH2_KEY = os.getenv('SOCIAL_AUTH_VK_OAUTH2_KEY')
SOCIAL_AUTH_VK_OAUTH2_SECRET = os.getenv('SOCIAL_AUTH_VK_OAUTH2_SECRET')
SOCIAL_AUTH_VK_OAUTH2_SCOPE = ["email"]
SOCIAL_AUTH_VK_OAUTH2_EXTRA_DATA = ["first_name", "last_name"]
#
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')
# SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
#     'https://www.googleapis.com/auth/userinfo.email',
#     'https://www.googleapis.com/auth/userinfo.profile',
#     'openid'
# ]
#
# SOCIAL_AUTH_GOOGLE_OAUTH2_EXTRA_DATA = ['first_name', 'last_name']

SOCIAL_AUTH_ALLOWED_REDIRECT_URIS = [
    "http://mysite.com/social/login/google-oauth2/",
    "http://mysite.com/social/complete/google-oauth2/",
]
