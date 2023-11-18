from django.db import models

# Create your models here.
class CornerImage(models.Model):
    picture = models.ImageField()
    info = models.CharField(max_length=200, blank=True)
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Corner Image took at {}".format(self.uploaded.strftime('%Y-%m-%d %H:%M'))