from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('emailanalysis.views',
    (r'^$', 'index'),
    (r'^(?P<datatype>[\w]+)/json/$', 'getjson'),

    (r'^login/submit/$', 'login_view'),
    (r'^login/$', 'login_view'),
    (r'^logout/$', 'logout_view'),
    (r'^results/$', 'results'),
    (r'^results_sent/$','results_sent'),
                       (r'^refresh/status/(\d+)/$', 'refresh_check'),
                       (r'^refresh/$', 'refresh_account'),
                       (r'^refresh/wait/(\d+)/$', 'refresh_wait'),
    (r'^loginfail/$', direct_to_template, {'template': 'emailanalysis/loginError.html'}),
    (r'^admin/', include(admin.site.urls)),
#    (r'^pie/$', 'pie'),                                              
#    (r'^sendmail/send/$', 'sendmail'),
#    (r'^test/$', direct_to_template, {'template': 'emailanalysis/testautocomplete.html'}),
#    (r'^testdate/$', direct_to_template, {'template': 'emailanalysis/testdateslider.html'}),
#   (r'^dash/$', direct_to_template, {'template': 'emailanalysis/dashboard.html'}),                       
#   (r'^home/$', 'index'),
#   (r'^createuser/$', 'create_user'),
#   (r'^createuser/submit/$', 'create_user'),
#    (r'^sendmail/$', 'sendmail'),
                       

    # Examples:
    # url(r'^$', 'liamgwebapp.views.home', name='urls return templatehome'),
    # url(r'^liamgwebapp/', include('liamgwebapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
