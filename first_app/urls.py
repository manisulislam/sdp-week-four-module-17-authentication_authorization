from django.urls import path

from . import views

urlpatterns = [
    path("", views.signUp, name="signUp"),
    path("signIn/", views.signIn, name="signIn"),
    path("sign_out/", views.sign_out, name="sign_out"),
    path("profile/", views.profile, name="profile"),
    path("password_change/", views.pass_change, name="passChange"),
    path("password_without_old/", views.without_old_pass_change, name="withoutOldPassChange"),
    path("update_data/", views.update_data, name="updateData"),
]
