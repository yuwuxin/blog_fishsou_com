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


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'url',
        'sort',
        'is_show',
        'created_at'
    )


admin.site.register(Category, CategoryAdmin)


class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'user_name',
        'other_name',
        'avatar',
        'sex',
        'email',
        'qq',
        'mobile_phone',
        'cps_type',
        'exp_value',
        'created_at'
    )


admin.site.register(Member, MemberAdmin)


class AdPositionAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'cover_img',
        'sort',
        'is_show',
        'created_at'
    )


admin.site.register(AdPosition, AdPositionAdmin)

admin.site.register(Message)


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'cover_img',
        'sort',
        'is_show',
        'created_at'
    )


admin.site.register(Tag, TagAdmin)


class LinkAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'url',
        'sort',
        'is_show',
        'created_at'
    )


admin.site.register(Link, LinkAdmin)
