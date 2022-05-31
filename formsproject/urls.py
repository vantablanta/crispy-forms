from django.contrib import admin
from django.urls import path, include

import formsapp 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('formsapp.urls')),
]
