from django.db import models

# Create your models here.
class RecentSearch(models.Model):
    city = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city