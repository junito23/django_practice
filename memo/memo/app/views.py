from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView, DeleteView
from django.urls import reverse, reverse_lazy

from .models import Memo


class MemoIndexView(ListView):
    template_name = 'app/index.html'
    model = Memo
    context_object_name = 'memos'
    # def index(self, request):
    #     memos = Memo.objects.all().order_by('-created_datetime')
    #     return render(request, self.template_name, {'memos', memos})
    def get_queryset(self):
        return Memo.objects.all().order_by('-created_datetime')

class MemoDetailView(DetailView):
    template_name = 'app/detail.html'
    model = Memo


class MemoCreateView(CreateView):
    template_name = 'app/new_memo.html'
    model = Memo
    fields = ("title", "text")
    # success_url = "/"
    def get_success_url(self):
        return reverse('app:detail', kwargs={'pk': self.object.pk})

class MemoDeleteView(DeleteView):
    model = Memo
    success_url = reverse_lazy('app:index')