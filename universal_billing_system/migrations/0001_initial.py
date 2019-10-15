# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-15 08:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255)),
                ('customer_phone', models.CharField(max_length=255)),
                ('customer_email', models.EmailField(max_length=255)),
                ('narration', models.CharField(max_length=255)),
                ('amount', models.FloatField()),
                ('quantity', models.FloatField(blank=True)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('bill_id', models.CharField(blank=True, max_length=120)),
                ('status', models.CharField(choices=[(0, 'Unpaid'), (1, 'Paid')], default='Unpaid', max_length=10)),
                ('generated_by', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Business_name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone_number', models.CharField(max_length=60)),
                ('Physical_address', models.CharField(max_length=60)),
                ('Post_code', models.CharField(max_length=20)),
                ('Town', models.CharField(max_length=20)),
                ('JP_paybill', models.CharField(max_length=20)),
                ('join_date', models.DateField(auto_now_add=True)),
                ('Business_owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Industry', models.ManyToManyField(to='universal_billing_system.Industry')),
            ],
        ),
        migrations.CreateModel(
            name='NewsLetterRecipients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('amount', models.FloatField(default=None)),
                ('quantity', models.FloatField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='NewsLetterRecipientss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payers_name', models.CharField(max_length=255)),
                ('payers_phone', models.CharField(max_length=255)),
                ('narration', models.CharField(max_length=255)),
                ('amount', models.FloatField()),
                ('pay_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Revstreams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='merchant',
            name='Revstreams',
            field=models.ManyToManyField(to='universal_billing_system.Revstreams'),
        ),
        migrations.AddField(
            model_name='bills',
            name='Revstreams',
            field=models.ManyToManyField(to='universal_billing_system.Revstreams'),
        ),
    ]
