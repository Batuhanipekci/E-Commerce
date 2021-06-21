from django.db import models


class KrDetailsView(models.Model):
    user = models.ForeignKey("KrUser", on_delete=models.CASCADE, db_column="kr_user_uuid")
    article = models.ForeignKey("KrArticle", on_delete=models.CASCADE, db_column="kr_article_id")
    ts = models.DateTimeField()

    class Meta:
        db_table = "kr_details_view"


class KrTransaction(models.Model):
    user = models.ForeignKey("KrUser", on_delete=models.CASCADE, db_column="kr_user_uuid")
    article = models.ForeignKey("KrArticle", on_delete=models.CASCADE, db_column="kr_article_id")
    order = models.ForeignKey("KrOrder", on_delete=models.CASCADE, db_column="kr_order_id", blank=True, null=True)
    ts = models.DateTimeField()

    class Meta:
        db_table = "kr_transaction"


# Connect to transaction signal
class KrCounter(models.Model):
    article = models.ForeignKey("KrArticle", on_delete=models.CASCADE, db_column="kr_article_id")
    details_view_count = models.IntegerField(null=False, blank=False, default=0)
    transaction_item_count = models.IntegerField(null=False, blank=False, default=0)
    ts_begin = models.DateTimeField()
    ts_end = models.DateTimeField()

    class Meta:
        db_table = 'kr_counter'
    
    def __str__(self):
        return f"{self.article.name}, detailViews: {self.details_view_count}, transaction_item: {self.transaction_item_count}"


class KrHighAttentionArticle(models.Model):
    article = models.ForeignKey("KrArticle", on_delete=models.CASCADE, db_column="kr_article_id")
    ts = models.DateTimeField()

    class Meta:
        db_table = "kr_high_attention_article"
    
    def __str__(self):
        return f"{self.article.id}-{self.ts}"
