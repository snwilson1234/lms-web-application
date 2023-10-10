from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class StudentAccountManager(BaseUserManager):

    def create_user(self, username, firstname, lastname, major, year, password=None):
        # if not email:
        #     raise ValueError("Email is required.")
        if not username:
            raise ValueError("Username is required.")
        if not firstname:
            raise ValueError("Student First Name is required.")
        if not lastname:
            raise ValueError("Student Last Name is required.")
        if not major:
            raise ValueError("Major is required.")
        if not year:
            raise ValueError("Year is required.")
        
        
        user = self.model(
            # email=self.normalize_email(email),
            username=username,
            firstname=firstname,
            lastname=lastname,
            major=major,
            year=year
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, firstname, lastname, major, year, password):
        user = self.create_user(
            # email=self.normalize_email(email),
            username=username,
            password=password,
            firstname=firstname,
            lastname=lastname,
            major=major,
            year=year
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class StudentAccount(AbstractBaseUser):
    # email           = models.EmailField(verbose_name="email",max_length=60, unique=True)
    
    user_id         = models.AutoField(primary_key=True)
    username        = models.CharField(max_length=30, unique=True)
    firstname       = models.CharField(max_length=60)
    lastname        = models.CharField(max_length=60)
    major           = models.CharField(max_length=100, unique=False)
    year            = models.DecimalField(max_digits=2,decimal_places=0)
    
    date_joined     = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['firstname','lastname','major','year']

    objects = StudentAccountManager()

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True