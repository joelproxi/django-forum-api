from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.
class CustomUserManager(BaseUserManager):
    use_in_migrations = True
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email requis")

        user = self.model(email=self.normalize_email(email=email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Le super utilisateur doit avoir is_satff = True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Le super utilisateur doit avoir is_superuser = True")
        
        return self.create_user(email, password, **extra_fields) 
            
            
class CustomUser(AbstractUser):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    object = CustomUserManager()
    
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['last_name', 'first_name']
    
    def __str__(self):
        return f'{self.last_name} {self.first_name}'
    
    def get_full_name(self) -> str:
        return super().get_full_name()
    