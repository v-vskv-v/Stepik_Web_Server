"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from qa.views import test, question_info, questions_new, questions_popular

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #,name='' -reverse routing
    url(r'^$', questions_new),
    url(r'^login/$', test),
    url(r'^signup/$', test),
    url(r'^question/(?P<q_id>\d+)/$', question_info, name='question-info'),
    url(r'^ask/$', test),
    url(r'^popular/$', questions_popular),
    url(r'^new/$', test),
]
