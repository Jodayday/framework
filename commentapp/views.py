from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from commentapp.forms import CommentCreateForm
from commentapp.models import Comment
from articleapp.models import Article
from django.contrib.auth.models import User

# Create your views here.


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreateForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        tem = form.save(commit=False)
        tem.article = Article.objects.get(
            pk=self.request.POST.get('article_pk'))
        tem.writer = self.request.user
        tem.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy('articleapp:detail', kwargs={'pk': self.object.article.pk})
