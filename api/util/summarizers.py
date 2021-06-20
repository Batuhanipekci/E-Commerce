from datetime import datetime, timedelta
from django.db import models
from django.apps import apps
from django.db import transaction
from api.util.iterators import increment_four_hours


def get_counter_config(article, ts):
    KrDetailsView = apps.get_model("api", "KrDetailsView")
    KrTransaction = apps.get_model("api", "KrTransaction")
    ts_begin = ts
    ts_end = ts + timedelta(hours=4)
    details_view_count = KrDetailsView.objects.filter(
        article=article,
        ts__gte=ts_begin,
        ts__lt=ts_end
    ).count()
    transaction_item_count = KrTransaction.objects.filter(
        article=article,
        ts__gte=ts_begin,
        ts__lt=ts_end,
        order__valid=True
    ).count()
    return({
        "article":article,
        "details_view_count":details_view_count,
        "transaction_item_count":transaction_item_count,
        "ts_begin":ts_begin,
        "ts_end":ts_end
    })


def increment_counter(article, ts):
    KrCounter = apps.get_model("api", "KrCounter")
    counter_dict = get_counter_config(article, ts)
    counter = KrCounter(**counter_dict)
    counter.save()
    print(f"Counter {counter.id} is saved to db at {ts}")


def populate_counter(ts_begin, ts_end):
    KrArticle = apps.get_model("api", "KrArticle")

    all_articles = KrArticle.objects.all()

    for article in all_articles:
        for ts in increment_four_hours(ts_begin, ts_end):
            increment_counter(article, ts)


@transaction.atomic
def populate_high_attention_article(ts_begin, ts_end):
    KrHighAttentionArticle = apps.get_model("api", "KrHighAttentionArticle")
    KrCounter = apps.get_model("api", "KrCounter")
    most_popular_100_article_count = KrCounter.objects.filter(ts_begin__lte=ts_begin, ts_end__lte=ts_end).order_by("-transaction_item_count")[:100]
    most_popular_100_articles = [instance.article for instance in most_popular_100_article_count]
    for article in most_popular_100_articles:
        high_attention_article = KrHighAttentionArticle.objects.create(article=article, ts=ts_end)
        print(f"{article.id} is a high-attention article between {ts_begin} and {ts_end}")
