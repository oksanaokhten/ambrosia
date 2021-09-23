from django.db import models


class News(models.Model):
    name = models.CharField(max_length=254)
    admin_name = models.CharField(max_length=50)
    admin_profession = models.CharField(max_length=50)
    text = models.TextField()
    image = models.ImageField(null=True, blank=True)
    date = models.DateTimeField('date published')

    def __str__(self):
        return self.name
