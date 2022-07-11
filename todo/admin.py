from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'priority', 'important', 'created']
    list_filter = ('important', 'status', 'priority')  
    readonly_fields = ('created',)
    

admin.site.register(Todo, TodoAdmin)
