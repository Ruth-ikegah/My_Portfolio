from django.db import models
from django_editorjs import EditorJsField

LABELS =(
    ("Speaking", "Speaking"),
    ("Project", "Project")
)
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
    title = models.CharField(max_length=200)
    label= models.CharField(choices=LABELS, blank=False, null=True, max_length=200)
    overview = EditorJsField(
        editorjs_config={
            "tools": {
                "Table": {
                    "disabled": False,
                    "inlineToolbar": True,
                    "config": {"rows": 2, "cols": 3,},
                }
            }
        }
    )
    image = models.ImageField()
    image_1 = models.URLField(blank=True, null=True)
    image_2 = models.URLField(blank=True, null=True)
    image_3 = models.URLField(blank=True, null=True)
    image_4 = models.URLField(blank=True, null=True)
    image_5 = models.URLField(blank=True, null=True)
    image_6 = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    slug = models.SlugField(blank=False, null=True)
    date = models.DateTimeField(auto_now_add=True,null=True,blank=True )

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ['title', 'slug']