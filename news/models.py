from django.db import models


class News(models.Model):

    class Meta:
        verbose_name_plural = "News"

    name = models.CharField(max_length=254)
    admin_name = models.CharField(max_length=50)
    admin_profession = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateTimeField('date published')
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
