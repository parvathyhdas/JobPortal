# Generated by Django 4.2.6 on 2023-10-29 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0003_alter_companydb_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CompanyName', models.CharField(blank=True, max_length=100, null=True)),
                ('JobTitle', models.CharField(blank=True, max_length=100, null=True)),
                ('PostedOn', models.CharField(blank=True, max_length=100, null=True)),
                ('ClosingOn', models.CharField(blank=True, max_length=100, null=True)),
                ('BriefDescription', models.CharField(blank=True, max_length=600, null=True)),
                ('PreferredSkills', models.CharField(blank=True, max_length=600, null=True)),
            ],
        ),
    ]
