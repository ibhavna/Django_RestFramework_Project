# Generated by Django 4.1.7 on 2023-03-18 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="school", name="updated_at",),
    ]
