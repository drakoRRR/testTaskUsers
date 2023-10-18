from django.views.generic import ListView, TemplateView


# Create your views here.
class UsersView(TemplateView):
    template_name = 'users/users_page.html'


class GroupsView(TemplateView):
    template_name = 'users/groups_page.html'


class EditUserView(TemplateView):
    template_name = 'users/edit_user_page.html'


class EditGroupView(TemplateView):
    template_name = 'users/edit_group_page.html'

