# Generated by Django 3.0.7 on 2020-06-10 00:04
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("water", "0006_order_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="comment",
            field=models.CharField(default="", max_length=500),
            preserve_default=False,
        ),
    ]
