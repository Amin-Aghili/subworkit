from django.db import models


class PublishedArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')
