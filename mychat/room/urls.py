
from django.conf import settings
from django.conf.urls.static import static
from django.urls import URLPattern


URLPattern += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)