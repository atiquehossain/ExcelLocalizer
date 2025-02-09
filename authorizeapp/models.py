from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
from django.contrib.auth.models import Group, Permission

class UserManager(BaseUserManager):
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=[
        ('developer', 'Developer'),
        ('ba', 'BA'),
        ('qa', 'QA')
    ])
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    # Specify unique related names to avoid clashes with the default User model
    groups = models.ManyToManyField(
        Group,
        related_name='authentication_user_set',  # Custom related_name for reverse lookup
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='authentication_user_permissions_set',  # Custom related_name for reverse lookup
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name']

    objects = UserManager()

    def __str__(self):
        return self.email
