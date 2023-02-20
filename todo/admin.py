from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'memo', 'important', 'created']
    list_filter = ('user', 'title', 'important')  
    readonly_fields = ('created',)
    

admin.site.register(Todo, TodoAdmin)
