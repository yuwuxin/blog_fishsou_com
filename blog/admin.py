from django.contrib import admin

# Register your models here.
from .models import Article
from .models import Category
from .models import Member
from .models import AdPosition


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'update_time',)


admin.site.register(Article, ArticleAdmin)

admin.site.register(Category)

admin.site.register(Member)

admin.site.register(AdPosition)
