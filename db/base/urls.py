from django.conf.urls import patterns, url

urlpatterns = patterns(
    'db.base.views',
    url(r'^$', 'home', name='home'),
    url(r'^suggestion/$', 'suggestion', name='suggestion'),
)
