# Generated by Django 2.0.12 on 2019-10-15 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universal_billing_system', '0007_merge_20191015_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bills',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
