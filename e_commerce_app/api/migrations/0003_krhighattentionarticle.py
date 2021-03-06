# Generated by Django 3.0.7 on 2021-06-20 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_event_redundancy'),
    ]

    operations = [
        migrations.CreateModel(
            name='KrHighAttentionArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ts', models.DateTimeField()),
                ('article', models.ForeignKey(db_column='kr_article_id', on_delete=django.db.models.deletion.CASCADE, to='api.KrArticle')),
            ],
            options={
                'db_table': 'kr_high_attention_article',
            },
        ),
    ]
