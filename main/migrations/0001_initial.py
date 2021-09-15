# Generated by Django 2.2.7 on 2021-09-14 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_link', models.CharField(max_length=100)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('long_link', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name_plural': 'Uploaded link Details',
            },
        ),
    ]
