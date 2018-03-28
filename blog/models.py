from django.db import models
import django


# Create your models here.
class Article(models.Model):
    title = models.CharField(u'标题', max_length=150)
    cover_img = models.ImageField(u'图片封面', max_length=200, default='', null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=1)
    click_count = models.PositiveIntegerField(u'点击数', default=0)
    user = models.ForeignKey('Member', on_delete=models.CASCADE, default=1)
    comment_count = models.PositiveIntegerField(u'评论数', default=0)
    praise_count = models.PositiveIntegerField(u'点赞数', default=0)
    sort = models.PositiveSmallIntegerField(u'排序', default=0)
    is_show = models.BooleanField(u'是否显示', default=1)
    is_hot = models.BooleanField(u'是否热门', default=0)
    is_top = models.BooleanField(u'是否置顶', default=0)
    is_essence = models.BooleanField(u'是否精华', default=0)
    description = models.TextField(u'描述', max_length=200, null=True)
    content = models.TextField(u'内容')
    created_at = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_at = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(u'标题', max_length=256)
    description = models.TextField(u'描述')
    created_at = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_at = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    def __str__(self):
        return self.title


class Member(models.Model):
    user_name = models.CharField(u'用户名', max_length=256)
    other_name = models.CharField(u'昵称', default='', max_length=256)
    email = models.EmailField(u'邮件', default='', max_length=100)
    avatar = models.CharField(u'头像', default='', max_length=100)
    password = models.CharField(u'密码', default='', max_length=100)
    salt = models.CharField(u'掩码', default='', max_length=100)
    qq = models.CharField(u'QQ', default=0, max_length=100)
    mobile_phone = models.CharField(u'手机', default=0, max_length=100)
    cps_type = models.CharField(u'用户类型', default=0, max_length=100)
    sex = models.CharField(u'性别', default=0, max_length=100)
    birthday = models.DateField(u'生日', default=0, max_length=100)
    exp_value = models.CharField(u'经验', default=0, max_length=100)
    description = models.TextField(u'描述', default='', max_length=200)
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


class Tag(models.Model):
    title = models.CharField(u'名称', max_length=256)
    description = models.TextField(u'描述')
    created_at = models.DateTimeField(u'创建时间', auto_now_add=True, editable=True)
    updated_at = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    def __str__(self):
        return self.title


class Link(models.Model):
    title = models.CharField(u'名称', max_length=256)
    url = models.CharField(u'网址', max_length=256)
    sort = models.PositiveIntegerField(u'排序', default=0)
    is_show = models.BooleanField(u'是否显示', default=1)
    description = models.TextField(u'描述')
    created_at = models.DateTimeField(u'创建时间', auto_now_add=True, editable=True)
    updated_at = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    def __str__(self):
        return self.title


class Message(models.Model):
    title = models.CharField(u'标题', max_length=256)
    user = models.CharField(u'用户', max_length=256)
    sort = models.PositiveIntegerField(u'排序', default=0)
    is_show = models.BooleanField(u'是否显示', default=1)
    description = models.TextField(u'留言内容')
    created_at = models.DateTimeField(u'创建时间', auto_now_add=True, editable=True)
    updated_at = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    def __str__(self):
        return self.title
