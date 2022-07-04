from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

from projectapp.models import Project
from projectapp.forms import ProjectCreateForm


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreateForm
    template_name = 'projectapp/create.html'

    def get_success_url(self) -> str:
        return reverse_lazy('projectapp:detail', kwargs={'pk': self.object.pk})


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'


class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 25
