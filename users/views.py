from django.http import HttpResponseRedirect
from django.views.generic import ListView, TemplateView

from users.forms import AddUserForm, AddGroupForm
from users.models import User, Group


# Create your views here.
class UsersView(ListView):
    model = User
    template_name = 'users/users_page.html'

    def post(self, request, *args, **kwargs):
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddUserForm()
        return context


class GroupsView(ListView):
    model = Group
    template_name = 'users/groups_page.html'

    def post(self, request, *args, **kwargs):
        form = AddGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddGroupForm()
        return context


class EditUserView(TemplateView):
    template_name = 'users/edit_user_page.html'


class EditGroupView(TemplateView):
    template_name = 'users/edit_group_page.html'

