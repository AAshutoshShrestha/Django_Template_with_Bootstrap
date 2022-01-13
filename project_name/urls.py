from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls import static
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),    
    path('home/',include('app_name.urls')),
    

    re_path(r'^statics/(?P<path>.*)$', serve, {
            'document_root': settings.STATIC_ROOT,
        }),
    re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),

]