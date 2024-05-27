from django.contrib import admin
from .models import ThesisProject

class ThesisProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic_num', 'title', 'superviser')
    list_filter = ('superviser',)
    search_fields = ('title', 'description')

admin.site.register(ThesisProject, ThesisProjectAdmin)