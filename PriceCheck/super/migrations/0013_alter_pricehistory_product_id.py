# Generated by Django 5.1 on 2024-09-16 02:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super', '0012_cartitem_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricehistory',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='super.product', to_field='product_code'),
        ),
    ]
