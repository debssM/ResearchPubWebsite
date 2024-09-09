from django.urls import path
from . import views

urlpatterns = [

    path('', views.drawbridge, name='Papers_index'),
    path('paperview/<p_id>', views.paper_view, name='Paper view')
]