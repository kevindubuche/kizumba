from django.db import models

# Create your models here.
class Dancer(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    # on chanhera ca en reel
    latitude = models.IntegerField()
    longitude = models.IntegerField()

    def is_a_valid_dancer(self):
        return (self.age >= 0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old; living at {self.address}."
