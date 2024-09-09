from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Paper Gallery Administration'

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('PaperCore.urls')),
    path(r'tracking/', include('tracking.urls')),
]
