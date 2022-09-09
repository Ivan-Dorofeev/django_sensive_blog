from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ('tags', 'likes', 'author')
    list_display = ['title', 'text', ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ('author',)
    list_display = ['post', 'text']
