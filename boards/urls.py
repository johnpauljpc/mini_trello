from django.urls import path
from .views import  CreateListBoard, DetailBoard

urlpatterns = [
    path("", CreateListBoard.as_view(), name="boards"),
    path("<slug>/", DetailBoard.as_view(), name="detail-board"),
]