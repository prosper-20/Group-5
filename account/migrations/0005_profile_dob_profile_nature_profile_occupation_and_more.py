# Generated by Django 4.2.13 on 2024-07-13 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_profile_shop'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='dob',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='profile',
            name='nature',
            field=models.CharField(choices=[('Supermarket', 'Supermarket'), ('Laundry', 'Laundry'), ('Pharmacy', 'Pharmacy'), ('Courier/Dispatch', 'Courier/Dispatch'), ('Banking/Insurance', 'Banking/Insurance'), ('Barbing/Salon', 'Barbing/Salon')], default='', max_length=25),
        ),
        migrations.AddField(
            model_name='profile',
            name='occupation',
            field=models.CharField(default='Plumber', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(default='', max_length=225),
        ),
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('new', 'new'), ('renewal', 'renewal'), ('exited', 'exited')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(default='10 Obe', max_length=225),
            preserve_default=False,
        ),
    ]
