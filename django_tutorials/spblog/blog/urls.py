from django.conf.urls.defaults import *

urlpatterns = patterns('',
  (r'^$', 'blog.views.index'),
  (r'^view/(?P<post_id>\d+)$', 'blog.views.view_post'),
)
