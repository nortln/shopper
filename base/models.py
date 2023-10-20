from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage


class AddressBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    image = models.ImageField(upload_to="img/users", storage=FileSystemStorage("base/static"))

    def __str__(self):
        return f"{self.address}"

class Brand(models.Model):
    brand = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.brand}"

class Catalog(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to="img/catalog", storage=FileSystemStorage("base/static"))

    def __str__(self):
        return f"{self.title}"
    


class Color(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="img/color", storage=FileSystemStorage("base/static"))

    def __str__(self):
        return f"{self.name}"




class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    cataglog = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    price = models.IntegerField()
    weight = models.IntegerField(default=None, null=True, blank=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, default=None, blank=True, null=True)
    image = models.ImageField(upload_to="img/products", storage=FileSystemStorage("base/static"), default=None)
    image2 = models.ImageField(upload_to="img/products", storage=FileSystemStorage("base/static"), default=None)
    image3 = models.ImageField(upload_to="img/products", storage=FileSystemStorage("base/static"), default=None)
    image4 = models.ImageField(upload_to="img/products", storage=FileSystemStorage("base/static"), default=None)

    def __str__(self):
        return f"{self.title}"




class Review(models.Model):
    title = models.CharField(max_length=50)
    review = models.TextField(max_length=500)
    rating = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


class CustomerCare(models.Model):
    available = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    social_1 = models.CharField(max_length=255, blank=True, null=True)
    social_2 = models.CharField(max_length=255, blank=True, null=True)
    social_3 = models.CharField(max_length=255, blank=True, null=True)
    social_4 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.available}"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    added_time = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.product} - {self.quantity}"