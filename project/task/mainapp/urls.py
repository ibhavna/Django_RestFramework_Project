from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("get_post_student/",student_one),
    path("put_delete_student/<int:id>/",student_two),
    path("get_post_school/",school_one),
    path("put_delete_school/<int:id>/",school_two),
    path("school_student_details/<int:id>/",get_school_data),
]
