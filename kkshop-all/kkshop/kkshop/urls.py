from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

app_name = 'kkshop'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('shop.urls', 'shop'), namespace='shop')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
