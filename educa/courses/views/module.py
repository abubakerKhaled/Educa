from django.views.generic.base import TemplateResponseMixin, View
from django.shortcuts import get_object_or_404, redirect
from ..models import Course
from ..forms import ModuleFormSet


class CourseModuleUpdateView(TemplateResponseMixin, View):
    template_name = 'courses/manage/module/formset.html'
    course = None

    def get_formset(self, data=None):
        return ModuleFormSet(instance=self.course, data=data)
    
    def dispatch(self, request, pk):
        self.course = get_object_or_404(
            Course, id=pk, owner=request.user
        )
        return super().dispatch(request, pk)
    
    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        context = {
            'course': self.course,
            'formset': formset
        }
        return self.render_to_response(context)
    
    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('manage-course-list')
        context = {
            'course': self.course,
            'formset': formset
        }
        return self.render_to_response(context)