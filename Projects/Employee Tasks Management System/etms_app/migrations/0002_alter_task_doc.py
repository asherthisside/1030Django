# Generated by Django 4.1.5 on 2023-07-31 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etms_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='doc',
            field=models.DateTimeField(null=True),
        ),
    ]
