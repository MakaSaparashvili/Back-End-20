Python 3.13.5

Exercise: Write Unit and View Tests for a Simple Blog App
Setup
You already have this model:

# models.py
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def short_title(self):
        return self.title[:10] + "..." if len(self.title) > 10 else self.title
And this view:

# views.py
from django.shortcuts import render
from .models import BlogPost

def post_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'posts/list.html', {'posts': posts})
✅ Your Task
Model Test

Write a test for short_title():

If title is less than 10 characters → returns full title.
If more → returns first 10 characters plus "...".
View Test

Write a test that checks:

The /posts/ page returns status code 200.
It contains the title of a blog post you've created in test setup.
