from django.contrib import admin

from .models import Client, Comment, TodoList

admin.site.register(Client)
admin.site.register(TodoList)
admin.site.register(Comment)