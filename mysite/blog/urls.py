from django.conf.urls import url
from blog import views
urlpatterns={
    url(r'^$',views.ListView.as_view(),name='post_list'),
    # url(r'^about/$',views.AboutView.as_view(),name='about'),
    # url(r"^post/(?p<pk>\d+)$",views.PostDetailView.as_view(),name='post_detail'),
    # url(r'^post/new/$',views.CreateView.as_view(),name ='post_new'),
    # url(r'^post/(?p<pk>\d+)/edit/$',views.UpdateView.as_view(),name="post_edit"),
    # url(r'^post/(?p<pk>\d+)/remove/$',views.PostDeleteView.as_view,name='post_remove'),
    # url(r'^Draft/$',views.PostDraftView.as_view(),name='Draft_list ')
}