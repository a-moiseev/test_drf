from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=512)
    date = models.DateTimeField(auto_now_add=True)
    md5 = models.CharField(max_length=16, editable=False)
    file = models.FileField(max_length=None)

    class Meta:
        ordering = ['date']
