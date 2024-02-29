from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .error_handlers import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls'), name='home'),  
    path('about/', include('about.urls'), name='about'), 
    path('contact/', include('contact.urls'), name='contact'), 
    path('markets/', include('markets.urls'), name='markets'),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += [
        path('404/', handler404, name='not_found'),

        path('500/', handler500, name='server_error'),
    ]
    
handler404 = handler404
handler500 = handler500