from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated', 'timestamp']
    list_display_links = ['updated']
    list_editable = ['title']
    list_filter = ['updated', 'timestamp']
    search_fields = ['title', 'content']

    class Meta:
        model = Project


admin.site.register(Project,ProjectModelAdmin)