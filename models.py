from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=255)

class Category(models.Model):
    name = models.CharField(max_length=255)

class Region(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    @property
    def has_town(self):
        town = Town.objects.filter(region=self).count()
        return bool(town)

class Town(models.Model):
    name  = models.CharField(max_length=255)
    country = models.ForeignKey(Region, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

class Place(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    town = models.ForeignKey(Town, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField()
    bio = models.TextField()
    working_hours = models.CharField(max_length=144)
    format = models.CharField(max_length=255)
    children_playing_room = models.CharField(max_length=255)
    hooka = models.BooleanField()
    alchoholic = models.BooleanField()
    veranda = models.BooleanField()
    balcon = models.BooleanField()
    music = models.BooleanField()
    breakfast = models.BooleanField()
    cash = models.IntegerField()
    # address = models.ManyToManyField(address)
    lat = models.CharField(max_length=255)
    lng = models.CharField(max_length=255)
    feedback = models.CharField(max_length=255)
    is_order_table = models.BooleanField()
