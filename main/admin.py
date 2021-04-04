from django.contrib import admin
from .models import Project,Profile

# Register your models here.
class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated', 'timestamp']
    list_display_links = ['updated']
    list_editable = ['title']
    list_filter = ['updated', 'timestamp']
    search_fields = ['title', 'description']

    class Meta:
        model = Project

admin.site.register(Project,ProjectModelAdmin)
admin.site.register(Profile)