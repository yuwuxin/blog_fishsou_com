from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(u'标题', max_length=150)
    cover_img = models.ImageField(u'图片封面', max_length=200, default='', null=True)
    category_id = models.PositiveIntegerField(u'分类', default=0)
    user_id = models.PositiveIntegerField(u'作者', default=0)
    click_count = models.PositiveIntegerField(u'点击数', default=0)
    comment_count = models.PositiveIntegerField(u'点击数', default=0)
    praise_count = models.PositiveIntegerField(u'点击数', default=0)
    sort = models.PositiveSmallIntegerField(u'点击数', default=0)
    is_show = models.BooleanField(u'是否显示', default=1)
    is_hot = models.BooleanField(u'是否热门', default=0)
    is_top = models.BooleanField(u'是否置顶', default=0)
    is_essence = models.BooleanField(u'是否精华', default=0)
    description = models.TextField(u'描述', max_length=200, null=True)
    content = models.TextField(u'内容')
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(u'标题', max_length=256)
    description = models.TextField(u'描述')

    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    def __str__(self):
        return self.title


class Member(models.Model):
    user_name = models.CharField(u'名称', max_length=256)
    description = models.TextField(u'描述')
    created_at = models.DateTimeField(u'创建时间', auto_now_add=True, editable=True)
    updated_at = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    def __str__(self):
        return self.user_name


class AdPosition(models.Model):
    title = models.CharField(u'名称', max_length=256)
    description = models.TextField(u'描述')
    created_at = models.DateTimeField(u'创建时间', auto_now_add=True, editable=True)
    updated_at = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    def __str__(self):
        return self.title
