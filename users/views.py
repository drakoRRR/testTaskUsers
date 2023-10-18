from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView

from users.forms import UserForm, GroupForm
from users.models import User, Group


# Create your views here.
class UsersView(ListView):
    model = User
    template_name = 'users/users_page.html'

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserForm()
        return context


class GroupsView(ListView):
    model = Group
    template_name = 'users/groups_page.html'

    def post(self, request, *args, **kwargs):
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = GroupForm()
        return context


class EditUserView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/edit_user_page.html'
    success_url = reverse_lazy('users:users')

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.kwargs.get('user_id'))

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class EditGroupView(UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'users/edit_group_page.html'
    success_url = reverse_lazy('users:groups')

    def get_object(self, queryset=None):
        return get_object_or_404(Group, pk=self.kwargs.get('group_id'))

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DeleteUserView(DeleteView):
    model = User
    success_url = reverse_lazy('users:users')

    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['user_id'])
        user.delete()

        return HttpResponseRedirect(self.success_url)


class DeleteGroupView(DeleteView):
    model = User
    success_url = reverse_lazy('users:groups')

    def get(self, request, *args, **kwargs):
        group = Group.objects.get(id=kwargs['group_id'])
        if not group.user_set.exists():
            group.delete()

        return HttpResponseRedirect(self.success_url)

