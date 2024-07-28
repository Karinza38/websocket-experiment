from django.urls import include, path

from notifications.counter.api.views import CounterView

app_name = "api"

urlpatterns = [
    path("v1/", include([path("counter/", CounterView.as_view(), name="counter")]))
]
