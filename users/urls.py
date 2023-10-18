from django.urls import path

from users.views import UsersView, GroupsView, EditUserView, EditGroupView, DeleteGroupView, DeleteUserView

app_name = 'users'

urlpatterns = [
    path('users/', UsersView.as_view(), name='users'),
    path('groups/', GroupsView.as_view(), name='groups'),
    path('edit-user/<int:user_id>', EditUserView.as_view(), name='edit-user'),
    path('edit-group/<int:group_id>', EditGroupView.as_view(), name='edit-group'),
    path('del-group/<int:group_id>', DeleteGroupView.as_view(), name='del-group'),
    path('del-user/<int:user_id>', DeleteUserView.as_view(), name='del-user'),
]
