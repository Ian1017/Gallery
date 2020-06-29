from django.db import models

#Create your models here.
class Location(models.Model):
    path = models.CharField(max_length=200)

    def __str__(self):
        return self.path

class Category(models.Models):
    IMAGE_CATEGORIES = (
        ('travel',"Travel"),
        ('food',"Food"),
        ('places',"Places")
    )
    category = models.CharField(max_lenght=20, choices=IMAGE_CATEGORIES)

    def __str__(self):
        return self.category

class Image(models.Model):
    image = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category)
    description = models.TextField()
    location = models.ForeignKey(Location)

    def __str__(self):
        return self.name



        