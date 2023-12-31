# Generated by Django 4.2.2 on 2023-07-11 19:18

from django.db import migrations
from django.core.management import call_command


def forwards_func(apps, schema_editor):
    call_command("loaddata", "courses")


def reverse_func(apps, schema_editor):
    News = apps.get_model("mainapp", "Courses")
    News.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_load_news_data'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
