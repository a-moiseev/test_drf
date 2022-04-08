from django.db import models
import hashlib


class Video(models.Model):
    title = models.CharField(max_length=512)
    date = models.DateTimeField(auto_now_add=True)
    md5 = models.CharField(max_length=16, editable=False)
    file = models.FileField(max_length=None)

    class Meta:
        ordering = ['date']

    def save(self, *args, **kwargs):
        """
        Расчет md5 при загрузке файла
        """
        if not self.pk:
            hash_md5 = hashlib.md5()
            for chunk in self.file.chunks():
                hash_md5.update(chunk)
            self.md5 = hash_md5.hexdigest()
        super(Video, self).save(*args, **kwargs)
