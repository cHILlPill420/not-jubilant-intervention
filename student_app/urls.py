from django.conf.urls import url
from student_app import views

app_name = 'student_app'

urlpatterns = [
    url(r'^schoollist/$', views.SchoolListView.as_view(), name = 'list'),
    url(r'^schoollist/(?P<pk>[-\w]+)/$', views.SchoolDetailView.as_view(), name = 'detail'),
    url(r'^create/$', views.SchoolCreateView.as_view(), name = 'create'),
    url(r'^schoollist/update/(?P<pk>[-\w]+)/$', views.SchoolUpdateView.as_view(), name = 'update'),
    url(r'^schoollist/delete/(?P<pk>[-\w]+)/$', views.SchoolDeleteView.as_view(), name = 'delete'),
]

#(?P<pk>[-\w]+)