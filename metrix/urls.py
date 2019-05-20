from django.conf.urls import url, include
from .views import ArticleView

urlpatterns = [
    url(r'^insert$', ArticleView.as_view()),
    url(r'^get_articles$', ArticleView.as_view()),
    url(r'^update_articles/(?P<pk>[0-9]+)/$', ArticleView.as_view()),
    url(r'^delete_articles/(?P<pk>[0-9]+)/$', ArticleView.as_view()),
]
