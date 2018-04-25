#!/usr/bin/env python
# _*_coding:utf-8_*_
# Author:li hang
from django import template
from ..models import Category, Article, Tag, Link

register = template.Library()


@register.inclusion_tag('widgets/header.html')
def pub_header():
    context = {
        'nav': Category.objects.all()
    }

    return context


@register.inclusion_tag('widgets/sidebar.html')
def pub_sidebar():
    recommend_list = Article.objects.filter(is_top=1)[:5]
    hot_list = Article.objects.filter(is_hot=1)[:5]
    tag_list = Tag.objects.all()
    link_list = Link.objects.all()
    contxt = {
        'recommend_list': recommend_list,
        'hot_list': hot_list,
        'tag_list': tag_list,
        'link_list': link_list
    }

    return contxt
