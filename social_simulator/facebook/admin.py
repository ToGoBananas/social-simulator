from django.contrib import admin

from .models import FacebookPost, Comment, FacebookPostLikes

admin.site.register(FacebookPost)
admin.site.register(Comment)
