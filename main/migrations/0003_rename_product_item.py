# Generated by Django 4.2.5 on 2023-09-26 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_delete_item'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Item',
        ),
    ]
