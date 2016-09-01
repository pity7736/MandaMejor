from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'mandadas/$', views.MandadasView.as_view()),
    url(r'mandadas/search/date/(?P<init_date>\d{4}-\d{2}-\d{2})/(?P<end_date>\d{4}-\d{2}-\d{2})/$', views.MandadasView.as_view()),
    url(r'mandadas/search/user/(?P<user_id>\d+)º/$', views.MandadasView.as_view()),
]
