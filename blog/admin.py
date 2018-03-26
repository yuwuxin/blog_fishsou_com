from django.contrib import admin
from blog.models import article


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'cover_img',
        'category_id',
        'user_id',
        'user_name',
        'click_count',
        'comment_count',
        'praise_count',
        'sort',
        'is_show',
        'is_hot',
        'is_top',
        'is_essence',
        'description',
        'content',
        'created_at'
    ]


admin.site.register(article, ArticleAdmin)
