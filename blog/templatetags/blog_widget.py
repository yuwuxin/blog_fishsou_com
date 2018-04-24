#!/usr/bin/env python
# _*_coding:utf-8_*_
# Author:li hang
from django import template
from ..models import Category

register = template.Library()

@register.inclusion_tag('widgets/header.html')
def pub_header():

    context = {
        'nav': Category.objects.all(),
    }
    return context
