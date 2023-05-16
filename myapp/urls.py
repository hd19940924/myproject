# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/5/15 11:47
# @filename :urls.py.py
# 开发工具 ：PyCharm
#from django.conf.urls
from django.urls import path,include
#import path, include
#import views
from . import views
urlpatterns = [
    path(r'add_book$', views.add_book, ),
    path(r'show_books$', views.show_books, ),
    #path('add_book/',views.add_book,name='add_book')
]