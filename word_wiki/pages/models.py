from django.db import models

from django.db import models

class Page(models.Model):
    word = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.word

