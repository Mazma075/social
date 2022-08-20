from django.contrib import admin
from . import models
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug', 'updated')
    list_filter = ('created',)
    search_fields = ('slug', 'body')
    raw_id_fields = ('user',)
    prepopulated_fields = {'slug':('body',)}

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','post','created','is_reply')
    raw_id_fields = ('user','post','reply')
admin.site.register(models.Vote)

