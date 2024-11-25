from django import forms
from django.core.exceptions import ValidationError

from .models import LeaveApplication


class LeaveApplicationForm(forms.ModelForm):
    class Meta:
        model = LeaveApplication
        fields = ["start_date", "end_date", "reason"]
        widgets = {
            "start_date": forms.TextInput(attrs={"class": "form-control datepicker"}),
            "end_date": forms.TextInput(attrs={"class": "form-control datepicker"}),
            "reason": forms.Textarea(attrs={"class": "form-control"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date and start_date > end_date:
            raise ValidationError("The start date cannot be after the end date.")
        return cleaned_data
