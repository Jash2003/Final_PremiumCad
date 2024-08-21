# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Blogpost(models.Model):
    title = models.TextField()
    readtime = models.IntegerField(default=2)
    date = models.DateField()
    coverimage = models.ImageField(upload_to="blog_covers")
    content = RichTextField()


def __str__(self):
        return self.title

class Applicant(models.Model):
      jobrole = models.TextField()
      name = models.TextField()
      email = models.TextField()
      phone = models.TextField()
      location = models.TextField()
      experience = models.TextField()
      resume = models.FileField(upload_to="resumes")

class Joblisting(models.Model):
      jobtitle = models.TextField()
      jobimage = models.ImageField(upload_to="joblisting_images")
      jobdescription = RichTextField()
      openpositions = models.IntegerField()
      location = models.TextField(default="Noida")
      department = models.TextField(default="Management")
      reports_to = models.TextField(default="")

      
      



      


