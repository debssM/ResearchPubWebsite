from django.shortcuts import render
from .models import PaperDetail, Diagram, Title

def drawbridge(request):
    qset = PaperDetail.objects.all()
    latest_title = Title.objects.all().order_by('-created_time')[0]
    return render(request, 'PaperCore/search_page.html', {'paperset': qset, 'title': latest_title})

def paper_view(request, p_id):
    details = PaperDetail.objects.get(id=p_id)
    diagrams = Diagram.objects.filter(paper=details)
    return render(request, 'PaperCore/details_view.html', {'details': details, 'diagrams': diagrams})