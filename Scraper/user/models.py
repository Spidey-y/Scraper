from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, phone_number, address, email, password, is_staff=False,is_active=True,
                    is_superuser=False):
        if not email:
            raise ValueError('User must have email')
        if not first_name:
            raise ValueError('User must have first name')
        if not last_name:
            raise ValueError('User must have last name')
        if not phone_number:
            raise ValueError('User must have phone number')
        if not address:
            raise ValueError('User must have address')
        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.phone_number = phone_number
        user.address = address
        user.set_password(password)
        user.is_staff = is_staff
        user.is_active = True
        user.is_superuser = is_superuser
        user.save()
        return user

    def create_superuser(self, first_name, last_name, phone_number, address, email, password):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True,
            address=address,
            is_active=True,
            phone_number=phone_number
        )
        user.save()
        return user


class User(AbstractUser):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    phone_number = models.CharField(max_length=13, blank=False, null=False, unique=True)
    address = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, null=False, unique=True)
    password = models.CharField(max_length=255, blank=False, null=False)
    objects = UserManager()
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'phone_number',
        'address',
    ]

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
