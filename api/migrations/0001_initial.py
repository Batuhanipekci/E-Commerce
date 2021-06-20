# Generated by Django 3.0.7 on 2021-06-20 19:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KrArticle',
            fields=[
                ('id', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('desc', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'kr_article',
            },
        ),
        migrations.CreateModel(
            name='KrEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('desc', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'kr_event',
            },
        ),
        migrations.CreateModel(
            name='KrOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales_revenue', models.FloatField()),
                ('valid', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'kr_order',
            },
        ),
        migrations.CreateModel(
            name='KrUser',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(blank=True, max_length=128, null=True)),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'db_table': 'kr_user',
            },
        ),
        migrations.CreateModel(
            name='KrTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ts', models.DateTimeField()),
                ('article', models.ForeignKey(db_column='kr_article_id', on_delete=django.db.models.deletion.CASCADE, to='api.KrArticle')),
                ('event', models.ForeignKey(db_column='kr_event_id', on_delete=django.db.models.deletion.CASCADE, to='api.KrEvent')),
                ('order', models.ForeignKey(blank=True, db_column='kr_order_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.KrOrder')),
                ('user', models.ForeignKey(db_column='kr_user_uuid', on_delete=django.db.models.deletion.CASCADE, to='api.KrUser')),
            ],
            options={
                'db_table': 'kr_transaction',
            },
        ),
        migrations.CreateModel(
            name='KrSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_view_count', models.IntegerField()),
                ('transaction_count', models.IntegerField()),
                ('total_sales_revenue', models.IntegerField()),
                ('ts_begin', models.DateTimeField()),
                ('ts_end', models.DateTimeField()),
                ('article', models.ForeignKey(db_column='kr_article_id', on_delete=django.db.models.deletion.CASCADE, to='api.KrArticle')),
            ],
            options={
                'db_table': 'kr_summary',
            },
        ),
        migrations.CreateModel(
            name='KrDetailsView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ts', models.DateTimeField()),
                ('article', models.ForeignKey(db_column='kr_article_id', on_delete=django.db.models.deletion.CASCADE, to='api.KrArticle')),
                ('event', models.ForeignKey(db_column='kr_event_id', on_delete=django.db.models.deletion.CASCADE, to='api.KrEvent')),
                ('user', models.ForeignKey(db_column='kr_user_uuid', on_delete=django.db.models.deletion.CASCADE, to='api.KrUser')),
            ],
            options={
                'db_table': 'kr_details_view',
            },
        ),
        migrations.CreateModel(
            name='KrCounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('ts_begin', models.DateTimeField()),
                ('ts_end', models.DateTimeField()),
                ('article', models.ForeignKey(db_column='kr_article_id', on_delete=django.db.models.deletion.CASCADE, to='api.KrArticle')),
                ('event', models.ForeignKey(db_column='kr_event_id', on_delete=django.db.models.deletion.CASCADE, to='api.KrEvent')),
                ('user', models.ForeignKey(db_column='kr_user_uuid', on_delete=django.db.models.deletion.CASCADE, to='api.KrUser')),
            ],
            options={
                'db_table': 'kr_counter',
            },
        ),
    ]
