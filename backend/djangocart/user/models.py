from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class Usermanager(BaseUserManager):
    def create_user(self,username,email,password):
        if not email:
            raise ValueError("User must provide email")
        if not username:
            raise ValueError("User Must provide username")
        
        user=self.model(
          username=username,
          email=self.normalize_email(email),
         )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,username,email,password):
        user=self.create_user(
            username=username,
            email=self.normalize_email(email),
            password=password
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username=models.CharField(max_length=20,unique=True)
    email=models.EmailField(unique=True,max_length=20)
    phonenumber=models.CharField(unique=True)
    #required fileds
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now_add=True)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now_add=True)
    is_staff=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']
    objects=Usermanager()
    def __str__(self):
        return self.email
    def has_perm(self,perm,obj=None):
        return self.is_superuser
    def has_module_perms(self,app_label):
        return True
    
