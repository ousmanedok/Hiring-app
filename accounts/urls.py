from django.urls import include, path

from .views import LoginView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("", include("django.contrib.auth.urls")),
]
