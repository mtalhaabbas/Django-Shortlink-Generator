from django.db import models

class Link(models.Model):
    name = models.CharField(max_length=200, blank=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    long_link = models.CharField(max_length=1000, blank=False)

    def __str__(self):
        return str(self.long_link)

    class Meta:
        verbose_name_plural = 'Uploaded link Details'


