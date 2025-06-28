from django.urls import path
from .views import RetrieveTaskView, ListCreateTaskView

urlpatterns = [
    path("", ListCreateTaskView.as_view()),
    path("<pk>/", RetrieveTaskView.as_view()),
]