"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
import myapp.urls
from myapp import views
#import myapp

urlpatterns = [
    path(r'^admin/', admin.site.urls),
  #  path(r'^api/', include(myapp.urls)),
  #  path(r'add_book/',myapp.urls.views.add_book),
    path(r'add_book/',views.add_book),
    path(r'^$', TemplateView.as_view(template_name="index.html")),
    #path(r'add_book/$', views.add_book, ),
    path('show_books/', views.show_books, ),
]
