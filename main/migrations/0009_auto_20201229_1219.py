# Generated by Django 3.1.4 on 2020-12-29 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20201129_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='is_working',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
