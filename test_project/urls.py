from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'test_project.views.test'),
)
