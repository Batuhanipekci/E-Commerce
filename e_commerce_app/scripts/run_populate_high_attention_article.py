from datetime import datetime, timedelta
from django.apps import apps
from api.util.iterators import increment_four_hours
from api.util.summarizers import populate_high_attention_article


KrDetailsView = apps.get_model("api", "KrDetailsView")

ts_begin = KrDetailsView.objects.all().order_by("ts")[0].ts
ts_end = KrDetailsView.objects.all().order_by("-ts")[0].ts


def run(*args):
    for ts in increment_four_hours(ts_begin, ts_end):
        populate_high_attention_article(ts, ts+timedelta(hours=4))