# Generated by Django 4.0.5 on 2022-06-06 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_customer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/profile/'),
        ),
    ]
