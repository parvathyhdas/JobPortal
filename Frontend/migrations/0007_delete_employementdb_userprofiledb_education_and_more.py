# Generated by Django 4.2.6 on 2023-11-23 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0006_userprofiledb_currentcompanyname_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EmployementDB',
        ),
        migrations.AddField(
            model_name='userprofiledb',
            name='Education',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userprofiledb',
            name='PassoutYear',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userprofiledb',
            name='University',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
