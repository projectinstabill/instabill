# Generated by Django 5.1 on 2024-08-29 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0021_remove_billeditem_dis'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
