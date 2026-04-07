from django.urls import path

from . import views

urlpatterns = [
    path("", views.operator_home, name="operator_home"),
    path("inspector/<str:session_id>/", views.session_inspector, name="session_inspector"),
    path("health/", views.health, name="health"),
    path("preview/client/", views.client_preview, name="client_preview"),
    path("preview/artifacts/", views.artifact_sample, name="artifact_sample"),
]
