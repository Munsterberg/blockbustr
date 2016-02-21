from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.movie_list, name='list'),
    url(r'(?P<pk>\d+)/$', views.show, name='show'),
]