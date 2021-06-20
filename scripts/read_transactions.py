import pandas as pd
import numpy as np
from django.apps import apps
from api.util.parsers import (
    parseArticles,
    parseEvents,
    parseUsers,
    parseOrders,
    parseTransactions,
    parseDetailsViews
)

filepath_valid = "/workspace/data/valid_transactions.csv"
filepath_views = "/workspace/data/views_transactions.csv"

print("Reading Data")
valid_transactions = pd.read_csv(filepath_valid)
views_transactions = pd.read_csv(filepath_views)

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

def run(*args):
    print("Parse Articles")
    article_dict = parseArticles(articleInstanceData)
    print("Parse Events")
    event_dict = parseEvents(eventInstanceData)
    print("Parse Users")
    user_dict = parseUsers(userInstanceData)
    print("Parse Orders")
    order_dict = parseOrders(orderInstanceData)
    print("Parse Transactions")
    parseTransactions(transactionInstanceData, user_dict, event_dict, article_dict, order_dict)
    print("Parse detailsViews")
    parseDetailsViews(detailsViewInstanceData, user_dict, event_dict, article_dict)
