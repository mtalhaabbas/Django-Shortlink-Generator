# Generated by Django 2.2.7 on 2021-09-14 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_link_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='short_link',
        ),
    ]