from django.conf.urls import patterns, include, url
from django.contrib import admin
from IdeaPublisher import views
from IdeaPublisher.forms import MyAuthenticationForm, ExampleForm

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'IdeaManagement.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^Hi$', 'IdeaPublisher.views.index', name='file_hi'),
    url(r'^$', views.IndexView.as_view(), name='file_index'),
    url(r'^Details$', views.details, name='details'),
    url(r'^AboutUs$', views.AboutUsView.as_view(), name='aboutUs'),
    url(r'^ContactUs$', views.ContactUsView.as_view(), name='contactUs'),
	url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'registration/login.html', 'authentication_form':MyAuthenticationForm, 'redirect_field_name':'/IdeaPublisher/'}, name='login'),
    url(r'^newUser/$', views.nuevo_usuario, name='newUser'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'file_index'}, name='logout'),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change', name='password_change',kwargs={
               'template_name': 'registration/password_change_form.html','password_change_form':ExampleForm,
               'post_change_redirect':'password_change_done',
               }),
    url(r'^password_change_done/$','django.contrib.auth.views.password_change_done',name='password_change_done',
        kwargs={'template_name': 'registration/password_change_done.html'}),
    url(r'^settings_change_done/$','django.contrib.auth.views.password_change_done',name='settings_change_done',kwargs={'template_name': 'registration/settings_change_done.html'}),
	url(r'^feedbacks$', views.FeedbackListView.as_view(), name="feedback_list"),
    url(r'^create/$', views.FeedbackCreateView.as_view(), name="feedback_create"),
    url(r'^update/(?P<feedback_pk>\d+)/$', views.FeedbackUpdateView.as_view(), name="feedback_update"),
    url(r'^delete/(?P<feedback_pk>\d+)/$', views.FeedbackDeleteView.as_view(), name="feedback_delete"),
    url(r'^searchPub/$', 'IdeaPublisher.ajax.searchPublicacion', name='searchPub'),
	url(r'^searchCrzIdea/$', 'IdeaPublisher.ajax.searchCrzIdea', name='searchCrzIdea'),
    url(r'^messages/', include('django_messages.urls')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^likes/', include('likes.urls')),
    url(r'^richcomments/', include('richcomments.urls')),
    url(r'^avatar/', include('avatar.urls')),
    url(r'^settings/$', views.UserEdit.as_view(), name='settings'),
    url(r'^createIdea/$', views.IdeaCreateView.as_view(), name="Idea_create"),
    url(r'^IdeaView/(?P<idea_pk>\d+)$', views.IdeaDetailView.as_view(), name='idea_view'),
	url(r'^updateIdea/(?P<idea_pk>\d+)/$', views.IdeaUpdateView.as_view(), name="Idea_update"),
    url(r'^deleteIdea/(?P<idea_pk>\d+)/$', views.IdeaDeleteView.as_view(), name="Idea_delete"),
    url(r'^Ideas$', views.IdeaListView.as_view(), name="ideas_list"),
    url(r'^MyIdeas$', views.MyIdeaListView.as_view(), name="myideas_list"),
	url(r'^get_ideas/', views.get_ideas, name='get_drugs'),
	url(r'^get_myideas/', views.get_myideas, name='get_mydrugs'),

)