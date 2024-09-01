from django.urls import path
from django.views.generic.base import TemplateView

from .views import CounterView, IncrementCounterView

app_name = "counter"

urlpatterns = [
    path("", TemplateView.as_view(template_name="base.html"), name="base"),
    path("counter/", CounterView.as_view(), name="counter"),
    path("increment/", IncrementCounterView.as_view(), name="increment"),
]
