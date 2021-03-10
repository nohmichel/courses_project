from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_course', views.new_course, name="new_course"),
    path('destroy:<int:course_id>', views.destroy, name='destroy'),
    path('delete_course:<int:course_id>', views.delete_course, name="delete_course"),
]