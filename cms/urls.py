# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from cms import views

urlpatterns = patterns('',
    # 書籍
    url(r'^book/$', views.book_list, name='book_list'),     # 一覧
    url(r'^book/add/$', views.book_edit, name='book_add'),  # 登録
    url(r'^book/mod/(?P<book_id>\d+)/$', views.book_edit, name='book_mod'),  # 修正
    url(r'^book/del/(?P<book_id>\d+)/$', views.book_del, name='book_del'),   # 削除

    # 感想
#     url(r'^impression/(?P<book_id>\d+)/$', views.impression_list, name='impression_list'),     # 一覧
    url(r'^impression/(?P<book_id>\d+)/$', views.ImpressionList.as_view(), name='impression_list'),  # 一覧
    url(r'^impression/add/(?P<book_id>\d+)/$', views.impression_edit, name='impression_add'),        # 登録
    url(r'^impression/mod/(?P<book_id>\d+)/(?P<impression_id>\d+)/$', views.impression_edit, name='impression_mod'),  # 修正
    url(r'^impression/del/(?P<book_id>\d+)/(?P<impression_id>\d+)/$', views.impression_del, name='impression_del'),   # 削除
)
