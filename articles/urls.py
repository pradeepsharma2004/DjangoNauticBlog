from django.conf.urls import url
from . import views

urlpatters = [
    url(r'^$', views.articles_list)

]

