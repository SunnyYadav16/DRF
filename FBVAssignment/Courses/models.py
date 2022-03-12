from django.db import models


# Create your models here.
class CourseModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    Discount = models.IntegerField(default=0)
    Duration = models.FloatField()
    Authorname = models.CharField(max_length=100)

    def __str__(self):
        return self.name
