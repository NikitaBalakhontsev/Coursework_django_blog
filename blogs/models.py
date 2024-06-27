from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    logo_url = models.URLField(null=True, blank=True)
    post_url = models.URLField()

    def __str__(self):
        return self.title