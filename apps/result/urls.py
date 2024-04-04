from django.urls import path
from .views import GradeAssignView, ViewGradesView

urlpatterns = [
    path("create/", GradeAssignView.as_view(), name="create-result"),
    path("view/", ViewGradesView.as_view(), name="view-result"),
]
