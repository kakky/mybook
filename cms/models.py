# -*- coding: utf-8 -*-
from django.db import models

class Book(models.Model):
    '''書籍'''
    name = models.CharField(u'書籍名', max_length=255)
    publisher = models.CharField(u'出版社', max_length=255, blank=True)
    page = models.IntegerField(u'ページ数', blank=True, default=0)
    
    def __str__(self):    # Python2: def __unicode__(self):
        return self.name
    
class Impression(models.Model):
    '''感想'''
    book = models.ForeignKey(Book, verbose_name=u'書籍', related_name='impressions')
    comment = models.TextField(u'コメント', blank=True)
    
    def __str__(self):    # Python2: def __unicode__(self):
        return self.comment
