# Generated by Django 2.0.12 on 2019-10-09 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universal_billing_system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletterrecipients',
            name='amount',
            field=models.FloatField(default=None),
        ),
        migrations.AddField(
            model_name='newsletterrecipients',
            name='quantity',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='bills',
            name='Revstreams',
            field=models.ManyToManyField(to='universal_billing_system.Revstreams'),
        ),
    ]
