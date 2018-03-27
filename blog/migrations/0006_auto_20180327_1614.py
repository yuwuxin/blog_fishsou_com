# Generated by Django 2.0.3 on 2018-03-27 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180327_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category_id',
            field=models.PositiveIntegerField(default=0, verbose_name='分类'),
        ),
        migrations.AlterField(
            model_name='article',
            name='click_count',
            field=models.PositiveIntegerField(default=0, verbose_name='点击数'),
        ),
        migrations.AlterField(
            model_name='article',
            name='comment_count',
            field=models.PositiveIntegerField(default=0, verbose_name='点击数'),
        ),
        migrations.AlterField(
            model_name='article',
            name='cover_img',
            field=models.ImageField(default='', max_length=200, null=True, upload_to='', verbose_name='图片封面'),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(max_length=200, null=True, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='article',
            name='is_essence',
            field=models.BooleanField(default=0, verbose_name='是否精华'),
        ),
        migrations.AlterField(
            model_name='article',
            name='is_hot',
            field=models.BooleanField(default=0, verbose_name='是否热门'),
        ),
        migrations.AlterField(
            model_name='article',
            name='is_show',
            field=models.BooleanField(default=1, verbose_name='是否显示'),
        ),
        migrations.AlterField(
            model_name='article',
            name='is_top',
            field=models.BooleanField(default=0, verbose_name='是否置顶'),
        ),
        migrations.AlterField(
            model_name='article',
            name='praise_count',
            field=models.PositiveIntegerField(default=0, verbose_name='点击数'),
        ),
        migrations.AlterField(
            model_name='article',
            name='sort',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='点击数'),
        ),
        migrations.AlterField(
            model_name='article',
            name='user_id',
            field=models.PositiveIntegerField(default=0, verbose_name='作者'),
        ),
    ]
