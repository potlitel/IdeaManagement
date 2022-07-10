from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from IdeaPublisher.forms import MyAuthenticationForm

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'IdeaManagement.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'registration/login.html', 'authentication_form':MyAuthenticationForm, 'redirect_field_name':'/IdeaPublisher/'}, name='login'),
    url(r'^IdeaPublisher/', include('IdeaPublisher.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
)
