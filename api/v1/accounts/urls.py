
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from rest_framework_nested.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register("", views.UsersViewset, basename="users")

urlpatterns = [
    path("login/", TokenObtainPairView.as_view()),
    path("login/refresh/", TokenRefreshView.as_view()),
    path("login/verify/", TokenVerifyView.as_view()),
    path("register/", views.RegisterUserView.as_view()),
    path("users/", include(router.urls)),
    path("user_profile/", views.RetriveUserData.as_view()),
]
