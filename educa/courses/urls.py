from django.urls import path
from . import views


urlpatterns = [
    path(
        'mine/',
        views.ManageCourseListView.as_view(),
        name='manage-course-list'
    ),
    path(
        'create/',
        views.CourseCreateView.as_view(),
        name='course-create'
    ),
    path(
        '<pk>/edit/',
        views.CourseUpdateView.as_view(),
        name='course-edit'
    ),
    path(
        '<pk>/delete/',
        views.CourseDeleteView.as_view(),
        name='course-delete'
    ),
    path(
        '<pk>/module/',
        views.CourseModuleUpdateView.as_view(),
        name='course-module-update'
    ),
    path(
        'module/<int:module_id>/content/<model_name>/create/',
        views.ContentCreateUpdateView.as_view(),
        name='module-content-create'
    ),
    path(
        'module/<int:module_id>/content/<model_name>/<id>/',
        views.ContentCreateUpdateView.as_view(),
        name='module-content-update'
    ),
    path(
        'content/<int:id>/delete/',
        views.ContentDeleteView.as_view(),
        name='module-content-delete'
    ),
    path(
        'module/<int:module_id>/',
        views.ModuleContentListView.as_view(),
        name='module-content-list'
    )
]
