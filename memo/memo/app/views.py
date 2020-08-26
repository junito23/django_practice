from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy
from .forms import MemoForm

from .models import Memo


class MemoIndexView(ListView):
    template_name = 'index.html'
    model = Memo
    context_object_name = 'memos'
    paginate_by = 5
    # def index(self, request):
    #     memos = Memo.objects.all().order_by('-created_datetime')
    #     return render(request, self.template_name, {'memos', memos})
    def get_queryset(self):
        return Memo.objects.all().order_by('-created_datetime')

class MemoDetailView(DetailView):
    template_name = 'detail.html'
    model = Memo


class MemoCreateView(CreateView):
    template_name = 'new_memo.html'
    model = Memo
    form_class = MemoForm
    # fields = ("title", "text")
    # success_url = "/"
    def get_success_url(self):
        return reverse('app:detail', kwargs={'pk': self.object.pk})

class MemoDeleteView(DeleteView):
    model = Memo
    success_url = reverse_lazy('app:index')

class MemoUpdateView(UpdateView):
    template_name = "edit_memo.html"
    # fields = ("title", "text")
    form_class = MemoForm
    model = Memo
    def get_success_url(self):
        return reverse('app:detail', kwargs={'pk': self.object.pk})