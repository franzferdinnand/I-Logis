# from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from transport.views import TransportListView, TransportProfileView

app_name = "transport"

urlpatterns = [
    path("", TransportListView.as_view(), name='transports'),
    path("transport-profile/<int:pk>", TransportProfileView.as_view(), name='transport_profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
