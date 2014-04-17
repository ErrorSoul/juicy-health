# coding: utf-8

from django.contrib import admin
from blog.models \
  import Post, Comment, Tag


class TagInline(admin.StackedInline):
    model = Tag

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ("views", "likes",)
    list_display=("title", "created","views","thumbnail")
    inlines  = [TagInline]

class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "created",)



class TagAdmin(admin.ModelAdmin):
    list_display = ('slug',)
    



admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)
