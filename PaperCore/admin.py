from .models import *
from django.contrib import admin
from django.utils.html import format_html

@admin.register(PaperDetail)
class PaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'additional_details', 'get_dataset')

    def get_dataset(self, obj):
        if obj.dataset_file:
            return format_html(f'<a class="" href={obj.dataset_file.url}>Download file</a>')
        else:
            return 'No file uploaded yet'
    get_dataset.short_description = 'Datasets'

@admin.register(Diagram)
class DiagramAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'paper', 'description', 'get_file')
    def get_file(self, obj):
        if obj.file:
            return format_html(f'<a class="" href={obj.file.url}>Download diagram</a>')
        else:
            return 'No file uploaded yet'

    get_file.short_description = 'Image file'

@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('page_title', 'created_time')