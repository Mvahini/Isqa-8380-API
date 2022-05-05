# Generated by Django 4.0.4 on 2022-05-05 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_package_lat_package_lng_alter_customer_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='lat',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='package',
            name='lng',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=10),
            preserve_default=False,
        ),
    ]