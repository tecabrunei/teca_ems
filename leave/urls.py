from django.contrib.auth import views as auth_views
from django.urls import path

from . import views


urlpatterns = [
    path("apply/", views.apply_leave, name="apply_leave"),
    path("status/", views.leave_status, name="leave_status"),
    path("manage/", views.manage_leaves, name="manage_leaves"),
    path("approve/<int:leave_id>/", views.approve_leave, name="approve_leave"),
    path("reject/<int:leave_id>/", views.reject_leave, name="reject_leave"),
    path("calendar/data/", views.leave_calendar_data, name="leave_calendar_data"),
    path("calendar/", views.calendar_view, name="calendar_view"),
    path("login/", auth_views.LoginView.as_view(template_name="leave/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("password_change/", auth_views.PasswordChangeView.as_view(template_name="leave/password_change.html"), name="password_change"),
    path("password_change_done/", auth_views.PasswordChangeDoneView.as_view(template_name="password_change_done.html"), name="password_change_done"),
]
