
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "ShikshaGo"
admin.site.site_title = "ShikshaGo Admin Panel"



urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('Blog.urls')),
    path('course/',include('Course.urls')),
    path('home/', include('Home.urls')),
    path('', include('Home.urls')),
] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)