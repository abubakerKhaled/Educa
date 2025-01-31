from django.urls import path
from . import views

urlpatterns = [
    path(
        'register',
        views.StudentRegistrationView.as_view(),
        name='student-registration'
    ),
    path(
        'enroll-course',
        views.StudentEnrollCourseView.as_view(),
        name='student-enroll-course'
    ),
]
