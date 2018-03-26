from django.db import models


# Create your models here.
class article(models.Model):
    title = models.CharField(max_length=150)
    cover_img = models.ImageField(max_length=200)
    category_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    user_name = models.CharField(max_length=25)
    click_count = models.PositiveIntegerField()
    comment_count = models.PositiveIntegerField()
    praise_count = models.PositiveIntegerField()
    sort = models.PositiveSmallIntegerField()
    is_show = models.BooleanField()
    is_hot = models.BooleanField()
    is_top = models.BooleanField()
    is_essence = models.BooleanField()
    description = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField()
