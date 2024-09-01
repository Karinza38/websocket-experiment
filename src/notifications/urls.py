from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("notifications.api.urls", namespace="api"), name="api"),
    path(
        "", include("notifications.counter.urls", namespace="counter"), name="counter"
    ),
]
