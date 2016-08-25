# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

#notify = False

class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    CATEGORIAS = (
        ("0", 'Anecdotas'),
        ("1", 'Momentos'),        
        ("2", 'Bailes'),
    )
    categorias = models.CharField(max_length=6,
                                      choices=CATEGORIAS,
                                      default="0")
    
    def __unicode__(self):
        return self.title





### Admin

class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    display_fields = ["title", "created","categorias"]
    
#NO IMPLEMENTADO    
class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body = models.TextField()
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return unicode("%s: %s" % (self.post, self.body[:60]))