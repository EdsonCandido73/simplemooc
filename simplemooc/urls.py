from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .core import views
from django.views.generic import TemplateView
admin.autodiscover()



urlpatterns = [
    path('', include('simplemooc.core.urls', namespace='core')),
    path('conta/', include('simplemooc.accounts.urls', namespace='accounts')),
    path('cursos/', include('simplemooc.courses.urls', namespace='courses')),
    path('forum/', include('simplemooc.forum.urls', namespace='forum')),
    path('admin/', admin.site.urls),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
       # Define a URL onde vai buscar as imagens (só usado no debug)

