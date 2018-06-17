from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('t_shirt', include('t_shirt.urls')),
    path('pullover', include('pullover.urls')),
    path('hoodie', include('hoodie.urls')),
    path('', include('main.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)