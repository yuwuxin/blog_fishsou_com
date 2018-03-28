# Generated by Django 2.0.3 on 2018-03-28 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180328_0649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='category_id',
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.PositiveIntegerField(default=0, verbose_name='Category'),
        ),
    ]
