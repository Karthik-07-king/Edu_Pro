# Generated by Django 4.2.16 on 2024-12-10 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("edu_core", "0010_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="duration",
            field=models.CharField(max_length=100),
        ),
    ]
