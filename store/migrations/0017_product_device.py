# Generated by Django 3.0.6 on 2020-06-16 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20200515_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='device',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
