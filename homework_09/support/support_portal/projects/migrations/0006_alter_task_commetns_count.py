# Generated by Django 3.2.4 on 2021-08-22 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_task_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='commetns_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
