from django.db import models
import textwrap


class PaperDetail(models.Model):
    title = models.CharField(max_length=500, null=False)
    authors = models.CharField(max_length=200)
    paper_link = models.CharField(max_length=200)
    description = models.TextField()
    additional_details = models.TextField()
    dataset_file = models.FileField(upload_to='static/datasets')

    def __str__(self):
        return textwrap.shorten(self.title, width=50)

class Diagram(models.Model):
    short_name = models.CharField(max_length=300)
    paper = models.ForeignKey(PaperDetail, on_delete=models.CASCADE, null=False)
    file = models.ImageField(upload_to='static/diagrams')
    description = models.TextField()

class Title(models.Model):
    page_title = models.CharField(max_length=100, null=False)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.page_title
