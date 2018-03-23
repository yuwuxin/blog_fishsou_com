from django.db import models

# Create your models here.
class article(models.Model):
    title = models.CharField(max_length=150)
    cover_img = ''
    category_id = ''
    description = models.TextField()
    content = models.TextField()
    cate = models.TextField()