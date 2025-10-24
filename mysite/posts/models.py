from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def short_title(self):
        return self.title[:10] + "..." if len(self.title) > 10 else self.title

    def __str__(self):
        return self.title
