# in model

from django.conf import settings
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL)


# in view

from django.contrib.auth import get_user_model
from django.shortcuts import render_to_response

def home(request):
    args = {}
    User = get_user_model()
    args['users'] = User.objects.all()
    render_to_response('home.html',args)



















