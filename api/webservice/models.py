import uuid
from django.db import models


class KrArticle(models.Model):
    # The article ids are big integers, Therefore they are set to VARCHAR
    id = models.CharField(unique=True, primary_key=True, max_length=128)
    name = models.CharField(max_length=128)
    desc = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        db_table = 'kr_article'

    def __str__(self):
        return self.name
    
    # The counter that will be visible in the UI (it will be sent in the response body to requests)
    @property
    def counter_detail_views(self):
        detail_views_list = KrCounter.objects.filter(article=self, event__name="detailsView").order_by("-ts")
        if len(detail_views_list)>0:
            return detail_views_list[0]
        else:
            return 0

    # The counter that will be visible in the UI (it will be sent in the response body to requests)
    @property
    def counter_transaction_item(self):
        transaction_item_list = KrCounter.objects.filter(article=self, event__name="transaction_item").order_by("-ts")
        if len(transaction_item_list)>0:
            return transaction_item_list[0]
        else:
            return 0

    # Capture the buy behaviour in the request body
    @property
    def buy(self):
        # Set default buy value
        return False
    
    # Expose if this is a high_attention article
    @property
    def higher_attention(self):
        pass


class KrEvent(models.Model):
    name = models.CharField(max_length=128)
    desc = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        db_table = 'kr_event'

    def __str__(self):
        return self.name


class KrUser(models.Model):
    # Note that Django Auth user is not inherited here, for simplicity
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=128, null=True, blank=True)
    password = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        db_table = 'kr_user'
    
    def __str__(self):
        return self.email


class KrOrder(models.Model):
    sales_revenue = models.FloatField()
    valid = models.BooleanField(default=False)

    class Meta:
        db_table = 'kr_order'

    def __str__(self):
        return self.id
    
