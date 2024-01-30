from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path


from cargo.views import CargoListView, CargoCreateView
from config.settings import dev

app_name = "cargo"

urlpatterns = [
    path(r"", CargoListView.as_view(), name='cargos'),
    path(r"create/", CargoCreateView.as_view(), name='create_cargos'),

] + static(dev.MEDIA_URL, document_root=dev.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()