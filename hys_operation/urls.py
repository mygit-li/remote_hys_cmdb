"""hys_cmdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from hys_operation import views

urlpatterns = [
    url(r'^sub_users/(?P<obj_id>\d+)', views.get_sub_users),
    url(r'^sub_servers/(?P<obj_id>\d+)', views.get_sub_servers),
    url(r'^download/(?P<paper_num>\w+)', views.download, name='download'),
]
