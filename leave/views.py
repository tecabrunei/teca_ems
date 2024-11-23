from datetime import timedelta

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import (
    redirect,
    render,
)
from django.contrib.auth.decorators import login_required

from .models import (
    LeaveApplication,
    Profile,
)
from .forms import LeaveApplicationForm


@login_required
def apply_leave(request):
    if request.method == "POST":
        form = LeaveApplicationForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.user = request.user
            leave.save()
            return redirect("leave_status")
        else:
            messages.error(request, "There were errors in your form. Please correct them.")
    else:
        form = LeaveApplicationForm()
    return render(request, "leave/apply_leave.html", {"form": form})


@login_required
def leave_status(request):
    leaves = LeaveApplication.objects.filter(user=request.user)
    return render(request, "leave/leave_status.html", {"leaves": leaves})


@login_required
def manage_leaves(request):
    if not hasattr(request.user, "profile") or request.user.profile.role != "manager":
        return redirect("leave_status")
    leaves = LeaveApplication.objects.filter(status="pending")
    return render(request, "leave/manage_leaves.html", {"leaves": leaves})


@login_required
def approve_leave(request, leave_id):
    leave = LeaveApplication.objects.get(id=leave_id)
    leave.status = "approved"
    leave.save()
    return redirect("manage_leaves")


@login_required
def reject_leave(request, leave_id):
    leave = LeaveApplication.objects.get(id=leave_id)
    leave.status = "rejected"
    leave.save()
    return redirect("manage_leaves")


@login_required
def leave_calendar_data(request):
    leaves = LeaveApplication.objects.filter(status="approved")
    data = [
        {
            "title": f"{leave.user.username} on leave",
            "start": leave.start_date.isoformat(),
            "end": (leave.end_date + timedelta(days=1)).isoformat(),
            "color": "blue",
        }
        for leave in leaves
    ]
    return JsonResponse(data, safe=False)


@login_required
def calendar_view(request):
    return render(request, "leave/calendar.html")
