# Generated by Django 4.1 on 2023-06-29 22:50

import colorfield.fields
from django.conf import settings
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True,
                        help_text="Введите имя",
                        max_length=100,
                        verbose_name="Имя",
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True,
                        help_text="Введите фамилию",
                        max_length=100,
                        verbose_name="Фамилия",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        help_text="Введите ваш e-mail",
                        max_length=254,
                        verbose_name="E-mail",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        help_text="Введите логин",
                        max_length=100,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="Логин",
                    ),
                ),
                (
                    "userpic",
                    models.ImageField(
                        blank=True,
                        help_text="Выберите изображение",
                        null=True,
                        upload_to="uploads/%Y/%m/%d/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["jpeg", "jpg", "png"]
                            )
                        ],
                        verbose_name="Фото пользователя",
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "Мужской"), ("female", "Женский")],
                        default="male",
                        help_text="Укажите ваш пол",
                        max_length=50,
                        verbose_name="Пол",
                    ),
                ),
                ("start_datetime", models.DateTimeField(auto_now_add=True)),
                ("last_datetime", models.DateTimeField(auto_now=True)),
                (
                    "latitude",
                    models.FloatField(
                        blank=True,
                        help_text="Укажите широту",
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(-90.1),
                            django.core.validators.MaxValueValidator(90.1),
                        ],
                        verbose_name="Широта",
                    ),
                ),
                (
                    "longitude",
                    models.FloatField(
                        blank=True,
                        help_text="Укажите широту",
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(-180.1),
                            django.core.validators.MaxValueValidator(90.1),
                        ],
                        verbose_name="Широта",
                    ),
                ),
            ],
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
        migrations.CreateModel(
            name="Status",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите статус",
                        max_length=50,
                        unique=True,
                        verbose_name="Текст статуса",
                    ),
                ),
            ],
            options={
                "verbose_name": "Статус",
                "verbose_name_plural": "Статусы",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите название",
                        max_length=50,
                        unique=True,
                        verbose_name="Название",
                    ),
                ),
                (
                    "color",
                    colorfield.fields.ColorField(
                        default="#FFFFFF",
                        image_field=None,
                        max_length=18,
                        samples=None,
                        unique=True,
                        verbose_name="Цвет",
                    ),
                ),
                ("slug", models.SlugField(unique=True, verbose_name="Ссылка")),
            ],
            options={
                "verbose_name": "Интерес",
                "verbose_name_plural": "Интересы",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="FriendsRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "current_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Текущий пользователь",
                    ),
                ),
                (
                    "friend",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="new_friend",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Друг",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FriendsRelationship",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "current_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="current_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Текущий пользователь",
                    ),
                ),
                (
                    "friend",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="friend",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Друг",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="customuser",
            name="friends",
            field=models.ManyToManyField(
                help_text="Укажите друзей",
                through="users.FriendsRelationship",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Друзья",
            ),
        ),
        migrations.AddField(
            model_name="customuser",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                related_name="user_set",
                related_query_name="user",
                to="auth.group",
                verbose_name="groups",
            ),
        ),
        migrations.AddField(
            model_name="customuser",
            name="status",
            field=models.ForeignKey(
                default=1,
                help_text="Укажите статус",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="statuses",
                to="users.status",
                verbose_name="Статус",
            ),
        ),
        migrations.AddField(
            model_name="customuser",
            name="tags",
            field=models.ManyToManyField(
                help_text="Выберите интересы",
                related_name="tags",
                to="users.tag",
                verbose_name="Интересы",
            ),
        ),
        migrations.AddField(
            model_name="customuser",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
        migrations.AddConstraint(
            model_name="friendsrequest",
            constraint=models.UniqueConstraint(
                fields=("current_user", "friend"),
                name="users_friendsrequest_unique_relationships",
            ),
        ),
        migrations.AddConstraint(
            model_name="friendsrequest",
            constraint=models.CheckConstraint(
                check=models.Q(("current_user", models.F("friend")), _negated=True),
                name="users_friendsrequest_prevent_self_add",
            ),
        ),
        migrations.AddConstraint(
            model_name="friendsrelationship",
            constraint=models.UniqueConstraint(
                fields=("current_user", "friend"),
                name="users_friendsrelationship_unique_relationships",
            ),
        ),
        migrations.AddConstraint(
            model_name="friendsrelationship",
            constraint=models.CheckConstraint(
                check=models.Q(("current_user", models.F("friend")), _negated=True),
                name="users_friendsrelationship_prevent_self_add",
            ),
        ),
    ]
