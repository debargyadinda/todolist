from django.contrib import admin
from django.urls import path, include  # Include tasks' urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),  # Include the tasks app's urls
]
