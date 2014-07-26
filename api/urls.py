# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from api import views

urlpatterns = patterns('',
    # 書籍
    url(r'^v1/books/$', views.book_list, name='book_list'),     # 一覧
)
