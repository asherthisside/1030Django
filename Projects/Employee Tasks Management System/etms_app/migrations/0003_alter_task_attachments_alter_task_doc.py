# Generated by Django 4.1.5 on 2023-08-01 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etms_app', '0002_alter_task_doc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='attachments',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='task',
            name='doc',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
