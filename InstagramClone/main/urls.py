from django.urls import path

from . import views

urlpatterns = {
    path("", views.default, name="home"),
    path("<str:username>", views.profile, name="profile"),
    path("direct/inbox/", views.inbox, name="inbox_messages"),
    #path("explore/", views.inbox, "explore"),
    #path("accounts/edit/", views.edit, "edit"),
}