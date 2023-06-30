from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.text import slugify
from django.contrib.auth import get_user_model
import uuid


class CustomUser(AbstractUser):
    fullname = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=50, default='')
    age = models.CharField(max_length=50, default='')
    gender = models.CharField(max_length=50, default='')
    country = models.CharField(max_length=50,default='0')
    accountbalance = models.CharField(max_length=50,default='0')
    profit = models.CharField(max_length=50,default='0')
    total_deposit = models.CharField(max_length=50,default='0')
    referal = models.CharField(max_length=50,default='0')
    total_withdrawal = models.CharField(max_length=50,default='0')
    rank = models.CharField(max_length=50,default='Beginner',blank=True)
    pro = models.BooleanField(default=False)
    image = models.ImageField(default='pro_ny6h2o.png',blank=True)
    is_email_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username
    
    def __str__(self):
        return self.username

class Pay_method(models.Model):
    name = models.CharField(max_length=50,default='0')
    wallet = models.CharField(max_length=500,default='0')
    image = models.ImageField(blank=True)
    visible = models.BooleanField(default=True)
    slug = models.SlugField(blank=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Pay_method, self).save(*args, **kwargs)

class Payment(models.Model):
    user = models.CharField(max_length=50,default='0')
    name = models.CharField(max_length=50,default='0')
    price = models.CharField(max_length=50,default='0')
    wallet = models.CharField(max_length=500,default='0')
    image = models.ImageField()
    approve = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Pin(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    pin = models.CharField(max_length=30, unique=True, blank=True)
    email = models.CharField(max_length=100, default='')
    active = models.BooleanField(default=False)
    approved = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    def __str__(self):
        return self.pin
class Withdraw(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    amount = models.CharField(max_length=30, blank=True)
    coin = models.CharField(max_length=30, blank=True)
    wallet = models.CharField(max_length=100, default='')
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username

class ChangePasswordCode(models.Model):
	user_email = models.EmailField(max_length=50)
	user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class ChangePassword(models.Model):
	new_password = models.CharField(max_length=50, blank = False, null = False)
	confirm_new_password = models.CharField(max_length=50, blank = False, null = False)

class Tran(models.Model):    
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    hash = models.CharField(default='7d2c7b06afa0 ...',max_length=200)
    amount = models.CharField(max_length=50, default='0')
    time = models.DateTimeField(blank=True,null=True)
    loss = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=(
        ('Success', 'Success'),
        ('In Progress', 'In Progress'),
        ('Failed', 'Failed'),      
        ),  default='Success')
    class Meta:
        ordering = ['-id']
    def __str__(self):
        return self.hash

class Trade(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    coin = models.CharField(max_length=30, unique=True, blank=True)
    ammount = models.CharField(max_length=100, default='')
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    def __str__(self):
        return self.coin

class Sta(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=50,default='0')
    price = models.CharField(max_length=50,default='0')
    wallet = models.CharField(max_length=500,default='0')
    approve = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Stake(models.Model):
    name = models.CharField(max_length=50,default='0')
    wallet = models.CharField(max_length=500,default='0')
    rate = models.CharField(max_length=50,default='0')
    image = models.ImageField()
    approve = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Plan(models.Model):
    name = models.CharField(max_length=50,default='0')
    profit = models.CharField(max_length=50,default='0')
    mindeposit = models.CharField(max_length=50,default='0')
    maxdeposit = models.CharField(max_length=50,default='0')
    duration = models.CharField(max_length=50,default='0')
    def __str__(self):
        return self.name

class Upgrade(models.Model):
    name = models.CharField(max_length=50,default='0')
    profit = models.CharField(max_length=50,default='0')
    mindeposit = models.CharField(max_length=50,default='0')
    def __str__(self):
        return self.name