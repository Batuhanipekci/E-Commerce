from api.util.summarizers import populate_counter
from django.apps import apps


KrDetailsView = apps.get_model("api", "KrDetailsView")

ts_begin = KrDetailsView.objects.all().order_by("ts")[0].ts
ts_end = KrDetailsView.objects.all().order_by("-ts")[0].ts


def run(*args):
    populate_counter(ts_begin, ts_end)
