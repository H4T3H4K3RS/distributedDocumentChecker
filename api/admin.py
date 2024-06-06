from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'created_at', 'updated_at')
    search_fields = ('status',)
    list_filter = ('status', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at',)

# @admin.register(Chunk)
# class ChunkAdmin(admin.ModelAdmin):
#     list_display = ('id', 'task', 'created_at', 'updated_at')
#     search_fields = ('task__id',)
#     list_filter = ('created_at', 'updated_at')
#     readonly_fields = ('id', 'created_at', 'updated_at')
