from django.db import models

# Create your models here.
class home(models.Model):
    name=models.CharField(max_length=250)
    place=models.CharField(max_length=250)
    img=models.ImageField(upload_to="gallery")
    price=models.CharField(max_length=250)

    def __str__(self):

        return self.name


