# Generated by Django 4.1.7 on 2023-03-18 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0003_school_updated_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="enrollment_no",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
