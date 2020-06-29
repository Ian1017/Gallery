from django.db import models
from django_countries.fields import CountryField




#Create your models here.
class Location(models.Model):
    country = CountryField(blank="select country")

    def __repr__(self):
        return self.country

class Category(models.Models):
    IMAGE_CATEGORIES = (
        ('travel', "Travel"),
        ('food', "Food"),
        ('places', "Places")
    )
    category = models.CharField(max_lenght=20, choices=IMAGE_CATEGORIES)

    def __str__(self):
        return self.category

class Image(models.Model):
    image = models.ImageField(upload_to='gallery/')
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category)
    description = models.TextField()
    location = models.ForeignKey(Location)

    def __str__(self):
        return self.name


