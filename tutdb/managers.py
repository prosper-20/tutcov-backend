from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)
from django.db import transaction
from django.contrib.auth import get_user_model
from django.conf import settings



class UserManager(BaseUserManager):
    def _create_user(self, email, username, password, **extra_fields):
        """ 
    Creates and saves a User with the given email,and password. 
"""
        if not email:
            raise ValueError('The given email must be set')
        try:
            with transaction.atomic():
                user = self.model(email=email, username=username, **extra_fields)
                user.set_password(password)
                user.save(using = self._db)
                return user
        except:
            raise

    
    def create_user(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        return self._create_user(email, username, password, **extra_fields)
    
    
    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        return self._create_user(email, username, password=password, **extra_fields)