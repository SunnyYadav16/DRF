from django.db import models


class InstructorModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.email


class CourseModel(models.Model):
    title = models.CharField(max_length=30)
    rating = models.FloatField()
    instructor = models.ForeignKey(InstructorModel, on_delete=models.CASCADE, related_name="courses")
