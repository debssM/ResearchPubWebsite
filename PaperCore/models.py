from PIL.ImageChops import blend
from django.db import models
import textwrap


class PaperDetail(models.Model):
    title = models.CharField(max_length=500, null=False)
    authors = models.CharField(max_length=200, null=True, blank=True)
    paper_link = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    additional_details = models.TextField(null=True, blank=True)
    dataset_file = models.FileField(upload_to='static/datasets',null=True, blank=True)

    def __str__(self):
        return textwrap.shorten(self.title, width=50)

class Diagram(models.Model):
    short_name = models.CharField(max_length=300)
    paper = models.ForeignKey(PaperDetail, on_delete=models.CASCADE, null=False)
    file = models.ImageField(upload_to='static/diagrams')
    description = models.TextField(null=True, blank=True)

class Title(models.Model):
    page_title = models.CharField(max_length=100, null=False)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.page_title
