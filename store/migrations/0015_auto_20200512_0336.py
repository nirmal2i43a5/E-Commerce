# Generated by Django 3.0.6 on 2020-05-12 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20200512_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Mens shoes and clothing', 'Mens shoes and clothing'), ('Womens shoes and clothing', 'Womens shoes and clothing'), ('Laptop', 'Laptop'), ('Desktop', 'Desktop'), ('Camera', 'Camera'), ('Mobile', 'Mobile'), ('Laptop accessories', 'Laptop accessories'), ('Storage', 'Storage'), ('Mobile accessories', 'Mobile accessories'), ('Audio', 'Audio'), ('Antivirus', 'Antivirus'), ('Camera accessories', 'Camera accessories'), ('Breakfast & Snacks', 'Breakfast & Snacks'), ('Wines,beers,& spirits', 'Wines,beers,& spirits'), ('Cooking ingredients', 'Cooking ingredients'), ('Kitchen,Dining, & Bedding', 'Kitchen,Dining, & Bedding'), ('Media,Books, & Music', 'Media,Books, & Music'), ('Watches', 'Watches'), ('Sunglasses & Eyeglasses', 'Sunglasses & Eyeglasses'), ('Make up & Body care', 'Make up & Body care'), ('Food supplements', 'Food supplements')], max_length=200, null=True),
        ),
    ]
