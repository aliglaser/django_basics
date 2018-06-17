from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from . import views


app_name = "courses"

urlpatterns = [
	path('', views.course_list, name="course_list"),
	path('<course_pk>/<step_pk>/', views.step_detail, name="step_detail"),
	path('<int:pk>/', views.course_detail, name="course_detail"),
]