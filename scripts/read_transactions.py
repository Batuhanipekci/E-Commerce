import pandas as pd
from django.apps import apps
from api.util.parsers import (
    preprocess_transaction_data,
    parseArticles,
    parseEvents,
    parseUsers,
    parseOrders,
    parseTransactions,
    parseDetailsViews,
)

filepath_valid = "/workspace/data/valid_transactions.csv"
filepath_views = "/workspace/data/views_transactions.csv"

print("Reading Data")
valid_transactions = pd.read_csv(filepath_valid)
views_transactions = pd.read_csv(filepath_views)

[
    articleInstanceData,
    eventInstanceData,
    userInstanceData,
    orderInstanceData,
    transactionInstanceData,
    detailsViewInstanceData,

]= preprocess_transaction_data(valid_transactions, views_transactions)

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