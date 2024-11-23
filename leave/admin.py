from django.contrib import admin

from .models import (
    LeaveApplication,
    Profile,
)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "role")
    list_filter = ("role",)


class LeaveApplicationAdmin(admin.ModelAdmin):
    list_display = ("user", "start_date", "end_date", "status", "applied_at")
    list_filter = ("status", "user")


admin.site.register(LeaveApplication, LeaveApplicationAdmin)
admin.site.register(Profile, ProfileAdmin)
