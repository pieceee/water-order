from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    volume = models.FloatField()
    price = models.FloatField()
    photo = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = (
        ('registered', 'registered'),
        ('confirmed', 'confirmed'),
        ('sent for delivery', 'sent for delivery'),
        ('delivered', 'delivered')
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='orders')
    place = models.CharField(max_length=100)
    date = models.DateTimeField()
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='')

    def __str__(self):
        return self.user.first_name + str(self.date)


class ProductOrder(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='orders')
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='products')
    count = models.IntegerField()

    def __str__(self):
        return "{} {} {}".format(self.product_id, self.order_id, self.count)


class Profile(models.Model):
    ROLE_CHOICES = (
        ('customer', 'customer'),
        ('manager', 'manager'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12)
    name = models.CharField(max_length=50)
    role = models.CharField(
        max_length=20, choices=ROLE_CHOICES, default='customer')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
