from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from profileapp.decorators import profile_ownership_required

# Create your views here.
from profileapp.forms import ProfileCreateForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    context_object_name = 'target_profile'
    success_url = reverse_lazy('accountapp:hi')
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        """form에서 제출한 값이 여기로 온다. """
        temp = form.save(commit=False)
        temp.user = self.request.user
        temp.save()
        return super().form_valid(form)


@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileCreateForm
    context_object_name = 'target_profile'
    success_url = reverse_lazy('accountapp:hi')
    template_name = 'profileapp/update.html'
