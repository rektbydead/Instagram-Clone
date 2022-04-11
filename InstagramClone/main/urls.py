from django.urls import path

from . import views

urlpatterns = {
    path("", views.default, name="home"),
    path("direct/inbox/", views.inbox, name="inbox_messages"),
    path("<str:profile_id>", views.profile, name="profile")
    #path("explore/", views.inbox, "explore"),
    #path("accounts/edit/", views.edit, "edit"),
}