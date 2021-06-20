import pandas as pd
import numpy as np
from django.apps import apps
from django.db import transaction


BATCHSIZE = 200000


def preprocess_transaction_data(valid_transactions, views_transactions):
    print("Data Preprocessing")
    articleInstanceData = views_transactions[["id"]].drop_duplicates()
    articleInstanceData["name"] = articleInstanceData["id"].copy()
    articleInstanceData["desc"] = np.nan

    eventInstanceData = views_transactions[["event_name"]].drop_duplicates()
    eventInstanceData["id"] = eventInstanceData["event_name"].copy()
    eventInstanceData["desc"] = np.nan

    userInstanceData = views_transactions[["user_id"]].drop_duplicates()
    userInstanceData["user_id"] = userInstanceData["user_id"].str.strip()
    userInstanceData["email"] = userInstanceData["user_id"] + "@user.com"
    userInstanceData["password"] = np.nan


    orderInstanceData = views_transactions[~views_transactions["order_id"].isna()].copy()
    orderInstanceData["order_id"] = orderInstanceData["order_id"].astype(int)
    orderInstanceData["valid"] = False
    orderInstanceData.loc[
        orderInstanceData["order_id"].isin(
        valid_transactions["order_id"].unique().tolist()
        ),"valid"] = True
    orderInstanceData = orderInstanceData[["order_id", "valid", "sales_revenue"]].drop_duplicates()

    transactionInstanceData = views_transactions[views_transactions['event_name']=='transaction_item'].copy()
    transactionInstanceData["order_id"] = transactionInstanceData["order_id"].astype(int)

    detailsViewInstanceData = views_transactions[views_transactions['event_name']=='detailsView'].copy()
    detailsViewInstanceData = detailsViewInstanceData.drop(["sales_revenue", "order_id"], axis=1)
    return (
        [
            articleInstanceData,
            eventInstanceData,
            userInstanceData,
            orderInstanceData,
            transactionInstanceData,
            detailsViewInstanceData
        ]
    )


# transaction.atomic decorator for bulk updates
@transaction.atomic
def parseArticles(instanceData):
    KrArticle = apps.get_model("api", "KrArticle")
    article_dict = {}
    for index, row in instanceData.iterrows():
        article = KrArticle()
        article.id = str(int(row["id"]))
        article.name = row["name"]
        article.desc = None if pd.isnull(row["desc"]) else row["desc"]
        
        article_dict[int(row["id"])] = article
    KrArticle.objects.bulk_create(list(article_dict.values()), BATCHSIZE)
    return article_dict


@transaction.atomic
def parseEvents(instanceData):
    KrEvent = apps.get_model("api", "KrEvent")
    event_dict = {}
    for index, row in instanceData.iterrows():
        event = KrEvent()
        event.name = row["event_name"]
        event.desc = None if pd.isnull(row["desc"]) else row["desc"]

        event_dict[row["id"]] = event
    KrEvent.objects.bulk_create(list(event_dict.values()), BATCHSIZE)
    return event_dict


@transaction.atomic
def parseUsers(instanceData):
    KrUser = apps.get_model("api", "KrUser")
    user_dict = {}
    for index, row in instanceData.iterrows():
        user = KrUser()
        user.uuid = row["user_id"].strip()
        user.email = row["email"]
        user.password = None if pd.isnull(row["password"]) else row["password"]

        user_dict[row["user_id"]] = user
    KrUser.objects.bulk_create(list(user_dict.values()), BATCHSIZE)
    return user_dict


@transaction.atomic
def parseOrders(instanceData):
    KrOrder = apps.get_model("api", "KrOrder")
    order_dict = {}
    for index, row in instanceData.iterrows():
        order = KrOrder()
        order.id = int(row["order_id"])
        order.sales_revenue = row["sales_revenue"]
        order.valid = row["valid"]

        order_dict[int(row["order_id"])] = order
    KrOrder.objects.bulk_create(list(order_dict.values()), BATCHSIZE)
    return order_dict


@transaction.atomic
def parseDetailsViews(instanceData, user_dict, event_dict, article_dict):
    KrDetailsView = apps.get_model("api", "KrDetailsView")
    detail_view_list = []
    for index, row in instanceData.iterrows():
        # For some reason bulk_create function doesn't work. This process can be optimized further.
        print("detailView: ", index)
        details_view = KrDetailsView.objects.create(
            user=user_dict[row["user_id"]],
            event=event_dict[row["event_name"]],
            article=article_dict[int(row["id"])],
            ts=row["ts"]
            )


@transaction.atomic
def parseTransactions(instanceData, user_dict, event_dict, article_dict, order_dict):
    KrTransaction = apps.get_model("api", "KrTransaction")
    transaction_list = []
    for index, row in instanceData.iterrows():
        # For some reason bulk_create function doesn't work. This process can be optimized further.
        print("Transaction: ", index)
        transaction_instance, transaction_instance_created  = KrTransaction.objects.get_or_create(
            user=user_dict[row["user_id"]],
            event=event_dict[row["event_name"]],
            article=article_dict[int(row["id"])],
            order=None if pd.isnull(row["order_id"]) else order_dict.get(int(row["order_id"])),
            ts=row["ts"]
            )