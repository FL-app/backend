from django.test import TestCase

from users.models import (CustomUser, CustomUserManager,
                          FriendsRequest, FriendsRelationship,
                          Tag)


# def user_test_create(name_prefix):
#     test_user = CustomUser.objects.create_user(
#         email=f'test_user_{name_prefix}@mail.com',
#         username=f'test_user_{name_prefix}',
#         password='Fa27hFm45',
#     )
#     return test_user


class CustomUserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        CustomUser.objects.create_user(
            email=f'test_user_1@mail.com',
            username=f'test_user_1',
            password='Fa27hFm45',
        )

    '''Testing DEFAULT_STATUS'''
    def test_DEFAULT_STATUS(self):
        user = CustomUser.objects.get(id=1)
        self.assertEqual(user.DEFAULT_STATUS, 'В сети')

    '''Testing MALE'''
    def test_MALE(self):
        user = CustomUser.objects.get(id=1)
        self.assertEqual(user.MALE, 'male')

    '''Testing FEMALE'''
    def test_FEMALE(self):
        user = CustomUser.objects.get(id=1)
        self.assertEqual(user.FEMALE, 'female')

    '''Testing ROLE_CHOICES'''
    def test_ROLE_CHOICES(self):
        user = CustomUser.objects.get(id=1)
        self.assertEqual(
            user.ROLE_CHOICES,
            [('male', "Мужской"), ('female', "Женский"),]
        )

    '''Testing first_name field'''
    def test_first_name_verbose_name(self):
        user = CustomUser.objects.get(id=1)
        verbose_name = user._meta.get_field('first_name').verbose_name
        self.assertEqual(verbose_name, 'Имя')

    def test_first_name_max_length(self):
        user = CustomUser.objects.get(id=1)
        max_length = user._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)

    def test_first_name_help_text(self):
        user = CustomUser.objects.get(id=1)
        help_text = user._meta.get_field('first_name').help_text
        self.assertEqual(help_text, 'Введите имя')

    def test_first_name_blank(self):
        user = CustomUser.objects.get(id=1)
        blank = user._meta.get_field('first_name').blank
        self.assertEqual(blank, True)

    '''Testing last_name field'''
    def test_last_name_verbose_name(self):
        user = CustomUser.objects.get(id=1)
        verbose_name = user._meta.get_field('last_name').verbose_name
        self.assertEqual(verbose_name, 'Фамилия')

    def test_last_name_max_length(self):
        user = CustomUser.objects.get(id=1)
        max_length = user._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 100)

    def test_last_name_help_text(self):
        user = CustomUser.objects.get(id=1)
        help_text = user._meta.get_field('last_name').help_text
        self.assertEqual(help_text, 'Введите фамилию')

    def test_last_name_blank(self):
        user = CustomUser.objects.get(id=1)
        blank = user._meta.get_field('last_name').blank
        self.assertEqual(blank, True)

    '''Testing email field'''
    def test_email_verbose_name(self):
        user = CustomUser.objects.get(id=1)
        verbose_name = user._meta.get_field('email').verbose_name
        self.assertEqual(verbose_name, 'E-mail')

    def test_email_help_text(self):
        user = CustomUser.objects.get(id=1)
        help_text = user._meta.get_field('email').help_text
        self.assertEqual(help_text, 'Введите ваш e-mail')

    def test_email_blank(self):
        user = CustomUser.objects.get(id=1)
        blank = user._meta.get_field('email').unique
        self.assertEqual(blank, True)

    '''Testing username field'''
    def test_username_verbose_name(self):
        user = CustomUser.objects.get(id=1)
        verbose_name = user._meta.get_field('username').verbose_name
        self.assertEqual(verbose_name, 'Логин')

    def test_username_max_length(self):
        user = CustomUser.objects.get(id=1)
        max_length = user._meta.get_field('username').max_length
        self.assertEqual(max_length, 100)

    def test_username_help_text(self):
        user = CustomUser.objects.get(id=1)
        help_text = user._meta.get_field('username').help_text
        self.assertEqual(help_text, 'Введите логин')

    def test_username_unique(self):
        user = CustomUser.objects.get(id=1)
        unique = user._meta.get_field('username').unique
        self.assertEqual(unique, True)

    def test_username_validators(self):
        user = CustomUser.objects.get(id=1)
        validators = user._meta.get_field('username').validators
        validator = validators[0].__class__.__name__
        self.assertEqual(validator, 'UnicodeUsernameValidator')

    '''Testing userpic field'''
    def test_userpic_verbose_name(self):
        user = CustomUser.objects.get(id=1)
        verbose_name = user._meta.get_field('userpic').verbose_name
        self.assertEqual(verbose_name, 'Фото пользователя')

    def test_userpic_help_text(self):
        user = CustomUser.objects.get(id=1)
        help_text = user._meta.get_field('userpic').help_text
        self.assertEqual(help_text, 'Выберите изображение')

    def test_userpic_blank(self):
        user = CustomUser.objects.get(id=1)
        blank = user._meta.get_field('userpic').blank
        self.assertEqual(blank, True)

    def test_userpic_null(self):
        user = CustomUser.objects.get(id=1)
        null = user._meta.get_field('userpic').null
        self.assertEqual(null, True)

    def test_userpic_upload_to(self):
        user = CustomUser.objects.get(id=1)
        upload_to = user._meta.get_field('userpic').upload_to
        self.assertEqual(upload_to, 'uploads/%Y/%m/%d/')

    def test_userpic_validators(self):
        user = CustomUser.objects.get(id=1)
        validators = user._meta.get_field('userpic').validators
        validator = validators[0].__class__.__name__
        self.assertEqual(validator, 'FileExtensionValidator')
        allowed_extensions = validators[0].allowed_extensions
        self.assertEqual(allowed_extensions, ["jpeg", "jpg", "png"])

    '''Testing tags field'''
    def test_tags_verbose_name(self):
        user = CustomUser.objects.get(id=1)
        verbose_name = user._meta.get_field('tags').verbose_name
        self.assertEqual(verbose_name, 'Интересы')

    def test_tags_help_text(self):
        user = CustomUser.objects.get(id=1)
        help_text = user._meta.get_field('tags').help_text
        self.assertEqual(help_text, 'Выберите интересы')

    def test_tags_related_name(self):
        self.fail("TODO Test incomplete")
        # user = CustomUser.objects.get(id=1)
        # related_name = user._meta.get_field('tags')
        # self.assertEqual(related_name, 'tags')

    def test_tags_adding_related_model(self):
        user = CustomUser.objects.get(id=1)
        related_model = user._meta.get_field('tags').related_model
        self.assertEqual(related_model.__name__, 'Tag')

    '''Testing status field'''
    def test_status_verbose_name(self):
        user = CustomUser.objects.get(id=1)
        verbose_name = user._meta.get_field('status').verbose_name
        self.assertEqual(verbose_name, 'Статус')

    def test_status_max_length(self):
        user = CustomUser.objects.get(id=1)
        max_length = user._meta.get_field('status').max_length
        self.assertEqual(max_length, 50)

    def test_status_help_text(self):
        user = CustomUser.objects.get(id=1)
        help_text = user._meta.get_field('status').help_text
        self.assertEqual(help_text, 'Укажите статус')

    def test_status_default(self):
        user = CustomUser.objects.get(id=1)
        default = user._meta.get_field('status').default
        self.assertEqual(default, 'В сети')

    '''Testing gender field'''
    def test_gender_verbose_name(self):
        user = CustomUser.objects.get(id=1)
        verbose_name = user._meta.get_field('gender').verbose_name
        self.assertEqual(verbose_name, 'Пол')

    def test_gender_max_length(self):
        user = CustomUser.objects.get(id=1)
        max_length = user._meta.get_field('gender').max_length
        self.assertEqual(max_length, 50)

    def test_gender_help_text(self):
        user = CustomUser.objects.get(id=1)
        help_text = user._meta.get_field('gender').help_text
        self.assertEqual(help_text, 'Укажите ваш пол')

    def test_gender_default(self):
        user = CustomUser.objects.get(id=1)
        default = user._meta.get_field('gender').default
        self.assertEqual(default, 'male')

    def test_gender_choices(self):
        user = CustomUser.objects.get(id=1)
        choices = user._meta.get_field('gender').choices
        self.assertEqual(
            choices,
            [('male', 'Мужской'), ('female', 'Женский')]
        )

    '''Testing start_datetime field'''
    def test_start_datetime_field_model(self):
        user = CustomUser.objects.get(id=1)
        start_datetime = user._meta.get_field('start_datetime')
        self.assertEqual(
            start_datetime.__class__.__name__,
            'DateTimeField'
        )

    def test_start_datetime_auto_now_add(self):
        user = CustomUser.objects.get(id=1)
        auto_now_add = user._meta.get_field('start_datetime').auto_now_add
        self.assertEqual(auto_now_add, True)

    '''Testing last_datetime field'''
    def test_last_datetime_field_model(self):
        user = CustomUser.objects.get(id=1)
        start_datetime = user._meta.get_field('last_datetime')
        self.assertEqual(
            start_datetime.__class__.__name__,
            'DateTimeField'
        )

    def test_last_datetime_auto_now_add(self):
        user = CustomUser.objects.get(id=1)
        auto_now = user._meta.get_field('last_datetime').auto_now
        self.assertEqual(auto_now, True)

    '''Testing latitude field'''
    def test_latitude_verbose_name(self):
        user = CustomUser.objects.get(id=1)
        verbose_name = user._meta.get_field('latitude').verbose_name
        self.assertEqual(verbose_name, 'Широта')

    def test_latitude_help_text(self):
        user = CustomUser.objects.get(id=1)
        help_text = user._meta.get_field('latitude').help_text
        self.assertEqual(help_text, 'Укажите широту')

    def test_latitude_blank(self):
        user = CustomUser.objects.get(id=1)
        blank = user._meta.get_field('latitude').blank
        self.assertEqual(blank, True)

    def test_latitude_null(self):
        user = CustomUser.objects.get(id=1)
        null = user._meta.get_field('latitude').null
        self.assertEqual(null, True)

    def test_latitude_validator_min_value(self):
        user = CustomUser.objects.get(id=1)
        validator_min = user._meta.get_field('latitude').validators[0]
        self.assertEqual(
            validator_min.__class__.__name__,
            'MinValueValidator'
        )
        self.assertEqual(validator_min.limit_value, -90.1)

    def test_latitude_validator_max_value(self):
        user = CustomUser.objects.get(id=1)
        validator_max = user._meta.get_field('latitude').validators[1]
        self.assertEqual(
            validator_max.__class__.__name__,
            'MaxValueValidator'
        )
        self.assertEqual(validator_max.limit_value, 90.1)

    '''Testing longitude field'''
    def test_longitude_verbose_name(self):
        user = CustomUser.objects.get(id=1)
        verbose_name = user._meta.get_field('longitude').verbose_name
        self.assertEqual(verbose_name, 'Долгота')

    def test_longitude_help_text(self):
        user = CustomUser.objects.get(id=1)
        help_text = user._meta.get_field('longitude').help_text
        self.assertEqual(help_text, 'Укажите долготу')

    def test_longitude_blank(self):
        user = CustomUser.objects.get(id=1)
        blank = user._meta.get_field('longitude').blank
        self.assertEqual(blank, True)

    def test_longitude_null(self):
        user = CustomUser.objects.get(id=1)
        null = user._meta.get_field('longitude').null
        self.assertEqual(null, True)

    def test_longitude_validator_min_value(self):
        user = CustomUser.objects.get(id=1)
        validator_min = user._meta.get_field('longitude').validators[0]
        self.assertEqual(
            validator_min.__class__.__name__,
            'MinValueValidator'
        )
        self.assertEqual(validator_min.limit_value, -180.1)

    def test_longitude_validator_max_value(self):
        user = CustomUser.objects.get(id=1)
        validator_max = user._meta.get_field('longitude').validators[1]
        self.assertEqual(
            validator_max.__class__.__name__,
            'MaxValueValidator'
        )
        self.assertEqual(validator_max.limit_value, 180.1)

    '''Testing friends field'''
    def test_friends_verbose_name(self):
        user = CustomUser.objects.get(id=1)
        verbose_name = user._meta.get_field('friends').verbose_name
        self.assertEqual(verbose_name, 'Друзья')

    def test_friends_help_text(self):
        user = CustomUser.objects.get(id=1)
        help_text = user._meta.get_field('friends').help_text
        self.assertEqual(help_text, 'Укажите друзей')

    def test_friends_through(self):
        self.fail("TODO Test incomplete")
        # user = CustomUser.objects.get(id=1)
        # through = user._meta.get_field('friends')
        # self.assertEqual(through, 'FriendsRelationship')

    '''Testing USERNAME_FIELD'''
    def test_USERNAME_FIELD(self):
        user = CustomUser.objects.get(id=1)
        value = user.USERNAME_FIELD
        self.assertEqual(value, 'email')

    '''Testing REQUIRED_FIELDS'''
    def test_REQUIRED_FIELDS(self):
        user = CustomUser.objects.get(id=1)
        value = user.REQUIRED_FIELDS[0]
        self.assertEqual(value, 'username')

    '''Testing model verbose_name'''
    def test_model_verbose_name(self):
        user = CustomUser.objects.get(id=1)
        self.assertEqual(user._meta.verbose_name, 'Пользователь')

    '''Testing model verbose_name_plural'''
    def test_model_verbose_name_plural(self):
        user = CustomUser.objects.get(id=1)
        self.assertEqual(
            user._meta.verbose_name_plural,
            'Пользователи'
        )

    '''Testing string representation'''
    def test_string_representation(self):
        user = CustomUser.objects.get(id=1)
        self.assertEqual(str(user), user.username)
