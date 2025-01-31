from django import forms
from courses.models import Course


class CourseEnrollForm(forms.Form):
    course = forms.ModelChoiceField(
        queryset=Course.objects.none(),
        widget=forms.HiddenInput
    )
    def __init__(self, *args, available_courses=None, **kwargs):
        super().__init__(*args, **kwargs)
        if available_courses is not None:
            self.fields['course'].queryset = available_courses