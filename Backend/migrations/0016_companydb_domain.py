# Generated by Django 4.2.6 on 2023-11-05 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0015_jobdb_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='companydb',
            name='Domain',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]