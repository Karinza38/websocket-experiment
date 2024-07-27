from django.db import models
from solo.models import SingletonModel


class GlobalCounter(SingletonModel):
    count = models.IntegerField(
        verbose_name="count", help_text="The value of the global counter", default=0
    )

    class Meta:
        verbose_name = "Global counter"

    def __str__(self) -> str:
        return "The global counter"
