from django.db import models


class Contact(models.Model):

    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=256, null=False, blank=False)
    message = models.TextField(max_length=600, null=False, blank=False)

    def __str__(self):
        return self.name
