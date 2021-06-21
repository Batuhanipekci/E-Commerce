from __future__ import absolute_import, unicode_literals
from datetime import timedelta
from django.utils import timezone
from celery import shared_task
from api.util.summarizers import (populate_counter, populate_high_attention_article)
from api.util.readers import read_transactions


@shared_task
def daily_data_load(filepath_valid, filepath_views):
    read_transactions(filepath_valid, filepath_views)

@shared_task
def counter_4h():
    ts_end = timezone.now()
    ts_begin = ts_end - timedelta(hours=4)
    populate_counter(ts_begin, ts_end)
    populate_high_attention_article(ts_begin, ts_end)
