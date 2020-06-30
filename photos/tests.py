from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.

class TestPhotosModels(TestCase):
    def setUp(self):
        self.new_category = Category(category="places")
        self.new_location = Location(country="AZ")
        self.new_image = Image(image="ray.jpeg",name="ray",category=self.new_category,description="ray pic",location=self.new_location)
    
    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

    def test_instances(self):
        self.assertTrue(isinstance(self.new_category, Category))
        self.assertTrue(isinstance(self.new_location, Location))
        self.assertTrue(isinstance(self.new_image, Image))

    def test_save_image(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_image(self):
        self.new_image.save_image()
        self.new_image.delete_image()
        images = Image.objects.all()        
        self.assertTrue(len(images) == 0)

    def test_location_find_category_id(self):
        location = Location.find_category_id("places")
        self.assertEquals(location,1)

    def test_search_image(self):
        location = Location.find_category_id("places")
        images = self.new_image.search_image(location)

        self.assertTrue(len(images) > 0)