from django.urls import path
from . import views

# the urls by which pages are called or accessed
urlpatterns = [
    path("", views.ApplicantsListView.as_view(), name="index"),
    path("add_applicant", views.ApplicantCreateView.as_view(), name="add"),
    path(
        "update_applicant/<int:pk>/", views.ApplicantUpdateView.as_view(), name="update"
    ),
    path(
        "delete_applicant/<int:pk>/", views.ApplicantDeleteView.as_view(), name="delete"
    ),
]
