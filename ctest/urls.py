from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ctest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),    

    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('capp.views',
 	url(r'^$', 'home', name='home'),
 	url(r'^log/$', 'get_log', name='getlog'),
 	url(r'^acode/$', 'addcode', name='addcode'),
)
