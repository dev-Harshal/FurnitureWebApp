from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class Users(AbstractUser):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith(('pbkdf2_sha256$', 'bcrypt$', 'argon2')):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)



class CartItem(models.Model):
    user = models.ForeignKey(Users, null=True, blank=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,null=True, blank=True)
    price = models.CharField(max_length=100,null=True, blank=True)
    image = models.CharField(max_length=100,null=True, blank=True)
    
class WishlistItem(models.Model):
    user = models.ForeignKey(Users, null=True, blank=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,null=True, blank=True)
    price = models.CharField(max_length=100,null=True, blank=True)
    image = models.CharField(max_length=100,null=True, blank=True)

class Feedback(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    feedback = models.CharField(max_length=100,null=True, blank=True)