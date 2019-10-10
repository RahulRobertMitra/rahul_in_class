from django.contrib import admin
from . import models

class PostAdmin(admin.ModelAdmin):
    list_display = (
    'title',
    'created',
    'updated'
    )
    search_fields = (
    'title',
    )
    pass

admin.site.register(models.Post, PostAdmin)
