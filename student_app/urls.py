from django.conf.urls import url
from student_app import views

app_name = 'student_app'

urlpatterns = [
    url(r'^schoollist/$', views.SchoolListView.as_view(), name = 'list'),
    url(r'^schooldetail/$', views.SchoolDetailView.as_view(), name = 'detail')
]