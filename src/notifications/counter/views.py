from django.conf import settings
from django.views.generic import TemplateView


class CounterView(TemplateView):
    template_name = "counter.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {"api_base_url": settings.API_BASE_URL, "ws_base_url": settings.WS_BASE_URL}
        )
        return context


class IncrementCounterView(TemplateView):
    template_name = "increment_counter.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"api_base_url": settings.API_BASE_URL})
        return context
