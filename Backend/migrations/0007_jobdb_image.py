# Generated by Django 4.2.6 on 2023-10-31 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0006_companydb_address_companydb_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobdb',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='Comp_Images'),
        ),
    ]
