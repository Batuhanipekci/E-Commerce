from datetime import datetime, timedelta


def increment_four_hours(start, finish):
    while finish > start:
        start = start + timedelta(hours=4)
        yield start