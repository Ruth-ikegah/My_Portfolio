from django.db import models


# Model for Contact
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

# Model for About
class About(models.Model):
    bio = models.TextField()
    

    def __str__(self):
        return self.bio

# Model for Projects and Work

class Work(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    problem_statement = models.TextField()
    image = models.ImageField()
    image_1 = models.ImageField()
    image_2 = models.ImageField()
    live_site = models.URLField(max_length=200)
    github_link = models.URLField(max_length=200)

    def __str__(self):
        return self.name

# Model for Speaking
class Speaking(models.Model):
    name = models.CharField(max_length=200)
    abstract = models.TextField()
    image = models.ImageField()
    slide_link = models.URLField(max_length=200)
    video_link = models.URLField(max_length=200)

    def __str__(self):
        return self.name

# Model for Speaking Calendar
class Calendar(models.Model):
    talk_title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date = models.DateField()
    register_link = models.URLField()

    def __str__(self):
        return self.talk_title




