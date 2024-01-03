# Generated by Django 4.2.6 on 2023-11-15 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Email', models.CharField(blank=True, max_length=50, null=True)),
                ('Mobile', models.IntegerField(blank=True, null=True)),
                ('ProfileImage', models.ImageField(blank=True, null=True, upload_to='ProfileImage')),
                ('Resume', models.FileField(blank=True, null=True, upload_to='document')),
                ('WorkStatus', models.CharField(choices=[('E', 'Experienced'), ('F', 'Fresher')], max_length=1)),
            ],
        ),
    ]
