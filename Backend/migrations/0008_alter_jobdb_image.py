# Generated by Django 4.2.6 on 2023-10-31 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0007_jobdb_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobdb',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='Images'),
        ),
    ]
