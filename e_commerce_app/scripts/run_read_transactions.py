import pandas as pd
from django.apps import apps
from api.util.readers import read_transactions


filepath_valid = "/workspace/data/valid_transactions.csv"
filepath_views = "/workspace/data/views_transactions.csv"


def run(*args):
    read_transactions(filepath_valid, filepath_views)