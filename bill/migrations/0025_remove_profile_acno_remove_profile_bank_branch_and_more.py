# Generated by Django 5.1 on 2024-08-29 17:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0024_remove_bank_type_bank_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='acno',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bank_branch',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bank_ifsc',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bank_name',
        ),
        migrations.AddField(
            model_name='profile',
            name='bank',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bill.bank'),
            preserve_default=False,
        ),
    ]
