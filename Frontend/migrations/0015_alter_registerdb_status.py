# Generated by Django 4.2.6 on 2023-12-27 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0014_alter_registerdb_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerdb',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]