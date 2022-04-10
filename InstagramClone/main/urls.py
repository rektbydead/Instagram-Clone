from django.urls import path

from . import views

url_pattern = {
    path("", views.default, name="home"),
    path("direct/inbox/", views.inbox, "inbox_messages"),
    path("<str:profile_id>", views.profile, "profile")
    #path("explore/", views.inbox, "explore"),
    #path("accounts/edit/", views.edit, "edit"),
}