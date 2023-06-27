from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    # author
    created_at = models.DateField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title + " | " + self.category.name
    
    @property
    def imageURL(self):
        url = ""
        try: 
            url = self.image.url
        except:
            url = ""

        return url 