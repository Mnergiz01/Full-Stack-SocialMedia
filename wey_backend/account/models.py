import uuid  
from django.contrib.auth.models import AbstractUser,PermissionsMixin,UserManager
from django.db import models
from django.utils import timezone
# Create your models here.

class CustomUserManager(UserManager):
        def create_user(self, email, password=None, **extra_fields):
            if not email:
                raise ValueError("The Email field must be set")
            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user
    
        def create_superuser(self, email, password=None, **extra_fields):
            extra_fields.setdefault("is_staff", True)
            extra_fields.setdefault("is_superuser", True)
    
            if extra_fields.get("is_staff") is not True:
                raise ValueError("Superuser must have is_staff=True.")
            if extra_fields.get("is_superuser") is not True:
                raise ValueError("Superuser must have is_superuser=True.")
    
            return self.create_user(email, password, **extra_fields)
        
class User(AbstractUser, PermissionsMixin):
    username=None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, blank=True, default='')
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    friend = models.ManyToManyField('self')

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True, blank=True)

    objects = CustomUserManager()
    

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

class FriendshipRequest(models.Model):
     SENT='sent'
     ACCEPTED='accepted'
     REJECTED='rejected'
     STATUS_CHOICES =(
          (SENT,'Sent'),
          (ACCEPTED,'Accepted'),
          (REJECTED,'Rejected'),

     )
     id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False) 
     created_for = models.ForeignKey(User,related_name='received_friendshiprequests',on_delete=models.CASCADE)
     created_at=models.DateTimeField(auto_now_add=True)
     created_by=models.ForeignKey(User,related_name='created_friendshiprequests',on_delete=models.CASCADE)
     status = models.CharField(max_length=30,choices=STATUS_CHOICES,default=SENT)

     
     
