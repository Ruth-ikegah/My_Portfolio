from django.db import models


# Model for Contact
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


# Model for Projects and Work

class Work(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    problem_statement = models.TextField()
    image = models.ImageField()
    image_1 = models.ImageField()
    image_2 = models.ImageField()
    live_site = models.URLField()
    github_link = models.URLField()
    slug = models.SlugField(blank=False, null=True)

    def __str__(self):
        return self.name
