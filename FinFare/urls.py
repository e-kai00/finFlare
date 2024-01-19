from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls'), name='home'),  
    path('about/', include('about.urls'), name='about'), 
    path('markets/', include('markets.urls'), name='markets'),  
] 
