# Generated by Django 4.2.13 on 2024-07-07 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_shop_address_shop_type_alter_shop_name'),
        ('account', '0002_customuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='shop',
            field=models.ManyToManyField(blank=True, null=True, to='shop.shop'),
        ),
    ]