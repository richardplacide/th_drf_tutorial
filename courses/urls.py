from django.urls import path, re_path
from . import views

urlpatterns = [
    path('/', views.ListCreateCourse.as_view()),
    re_path(r'(?P<pk>\d+)/$', views.RetrieveUpdateDestroyCourse.as_view()),
    re_path(r'(?P<course_pk>\d+)/reviews/$', views.ListCreateReview.as_view()),
    re_path(r'(?P<course_pk>\d+)/reviews/(?P<pk>\d+)/$',
         views.RetrieveUpdateDestroyReview.as_view()),   
]