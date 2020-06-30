from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url("^$",views.home,name="home"),
    url('^search/', views.search,name='search'),
    url('^location/', views.location, name='location'),
    url(r'^copy/(\d+)',views.copy_image, name='copy_image'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    