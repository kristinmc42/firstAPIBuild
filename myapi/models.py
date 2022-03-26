from django.db import models

# Create your models here.
# name and alias are character fields where strings can be stored
class Hero(models.Model):
  name = models.CharField(max_length=60)
  alias = models.CharField(max_length=60)

# __str__ method tells django what to print of an instance of the Hero model
  def __str__(self):
    return self.name