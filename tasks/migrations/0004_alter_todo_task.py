# Generated by Django 4.1.3 on 2022-11-22 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_todo_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='task',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
