from django.contrib import admin
from .models import Article
from embed_video.admin import AdminVideoMixin


@admin.register(Article)
class ArticleAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ('title', 'writer', 'publish', 'status')
    list_filter = ('status', 'publish', 'writer')
    list_editable = ('status',)
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    actions = ['make_published', 'make_draft']

