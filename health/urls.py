from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'health.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'hospitals.views.home', name='home'),
    url(r'^multi_field_search/', 'hospitals.views.multi_field_search', name='multi_field_search'),
    url(r'^query_city/', 'hospitals.views.query_city', name='query_city'),
    url(r'^query_hospital/', 'hospitals.views.query_hospital', name='query_hospital'),
    url(r'^submit_form/', 'hospitals.views.submit_form', name='submit_form'),
    url(r'^test', 'hospitals.views.test', name='test'),
)
