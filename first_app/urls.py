from django.urls import path

from . import views

urlpatterns = [
    path("", views.signUp, name="signUp"),
    path("signIn/", views.signIn, name="signIn"),
    path("sign_out/", views.sign_out, name="sign_out"),
    path("profile/", views.profile, name="profile"),
]
