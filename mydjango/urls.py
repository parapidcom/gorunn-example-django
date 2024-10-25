from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import home  # make sure to import the view function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Set the home view as the default route
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
