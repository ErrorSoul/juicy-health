#coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField


class AbstractDate(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
    

class AbstractTitleData(AbstractDate):
    title = models.CharField(max_length=200)

    class Meta:
        abstract = True

   
class Category(models.Model):
    title = models.CharField(max_length=60, unique=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/{0}".format(self.title).lower()
    

class Post(AbstractTitleData):
    body = RichTextField(config_name='default')
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    category = models.ForeignKey(Category)

    def thumbnail(self):
        return """<a href="/media/%s"><img border="0" alt=""
                  src="/media/%s" height="60" /></a>""" % ((self.picture.name, self.picture.name))
    thumbnail.allow_tags = True

    class Meta:
        ordering = ["-created"]

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        #return "/post/{0}".format(self.id)
        return reverse("blog:pt_detail", kwargs={"pk": self.pk})
        


class Tag(models.Model):
    slug = models.SlugField(max_length=15)
    post = models.ManyToManyField(Post, related_name="tags")

    def __unicode__(self):
        return self.slug


class Comment(AbstractDate):
    post = models.ForeignKey(Post, related_name="comments")
    author = models.CharField(max_length=25)
    body = models.TextField()
