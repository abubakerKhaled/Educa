from django.forms.models import inlineformset_factory
from .models import Module, Course


ModuleFormSet = inlineformset_factory(
    Course,
    Module,
    fields=['title', 'description'],
    extra=2,
    can_delete=True
)