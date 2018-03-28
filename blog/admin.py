from django.contrib import admin

# Register your models here.
from .models import Article
from .models import Category
from .models import Member
from .models import AdPosition
from .models import Message
from .models import Tag
from .models import Link


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'cover_img',
        'user_id',
        'click_count',
        'comment_count',
        'praise_count',
        'sort',
        'is_show',
        'created_at',
    )


admin.site.register(Article, ArticleAdmin)

admin.site.register(Category)

admin.site.register(Member)

admin.site.register(AdPosition)

admin.site.register(Message)

admin.site.register(Tag)

admin.site.register(Link)



