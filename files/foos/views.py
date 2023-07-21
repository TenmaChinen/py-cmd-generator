from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render
from foos.forms import FooForm
from foos.models import Foo

# CREATE
class FooCreateView(CreateView):
  form_class = FooForm
  template_name = 'foos/create.html'
  success_url = reverse_lazy('foos:list')

  def form_valid(self, form):
    if Foo.objects.exists():
      new_idx = Foo.objects.latest('idx').idx + 1
    else:
      new_idx = 1
    form.instance.idx = new_idx
    return super().form_valid(form)

  # def get_context_data(self, **kwargs):
  #     context = super().get_context_data(**kwargs)
  #     context['parent_id'] = self.kwargs['parent_id']
  #     return context


class FooDetailView(DetailView):
  model = Foo
  template_name = 'foos/detail.html'
  context_object_name = 'foo'


# Read
class FooListView(ListView):
  model = Foo
  template_name = 'foos/list.html'
  context_object_name = 'list_foo'
  
  # def get_queryset(self):
  #   queryset = super().get_queryset()
  #   foo_id = self.kwargs['parent_id']
  #   return queryset.filter(foo_id=foo_id)	

  # def get_context_data(self, **kwargs):
  #     context = super().get_context_data(**kwargs)
  #     context['parent'] = Training.objects.get( id=self.kwargs['parent_id'])
  #     return context

# Update
class FooUpdateView(UpdateView):
  model = Foo
  form_class = FooForm

  template_name = 'foos/update.html'
  success_url = reverse_lazy('foos:list')
  
  # def get_context_data(self, **kwargs):
  #     context = super().get_context_data(**kwargs)
  #     context['foo_id'] = self.object.foo.id
  #     return context

  # def form_valid(self, form):
  #    form.instance.foo_id = self.kwargs['foo_id']
  #    return super().form_valid(form)
  
  # def get_success_url(self):
  #    d_kwargs = { 'foo_id' : self.object.foo.id }
  #    return reverse_lazy('foos:list', kwargs=d_kwargs)


# Delete
class FooDeleteView(DeleteView):
  model = Foo
  template_name = 'foos/delete.html'
  success_url = reverse_lazy('foos:list')

  # def get_success_url(self):
  #   d_kwargs = { 'foo_id' : self.object.foo.id }
  #   return reverse_lazy('foos:list', kwargs=d_kwargs)