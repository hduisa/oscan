from django.conf.urls import patterns, url


urlpatterns = patterns('oscan.views',
    # Examples:
    # url(r'^$', 'sign.views.home', name='home'),
    # url(r'^sign/', include('sign.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    url(r'^$', 'main'),
    url(r'^scanqueue/$', 'scanqueue'),
    url(r'^results/$', 'results'),
    url(r'^settings/$', 'settings'),
)

