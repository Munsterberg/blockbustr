from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.movie_list, name='list'),
    url(r'^new/$', views.new, name='new'),
    url(r'(?P<pk>\d+)/$', views.show, name='show'),
    url(r'^comment/new/$', views.comment_new, name='comment_new'),
]
