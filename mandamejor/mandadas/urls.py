from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'mandadas/$', views.MandadasView.as_view()),
    url(r'mandadas/user/(?P<user_id>\d+)/$', views.MandadasByUserView.as_view())
]
