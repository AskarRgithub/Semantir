from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateTimeField()
    published = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title
