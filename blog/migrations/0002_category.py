# Generated by Django 2.0.3 on 2018-03-27 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='标题')),
                ('description', models.TextField(verbose_name='描述')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
        ),
    ]