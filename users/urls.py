from django.urls import path

from users.views import UsersView, GroupsView, EditUserView, EditGroupView

app_name = 'users'

urlpatterns = [
    path('users/', UsersView.as_view(), name='users'),
    path('groups/', GroupsView.as_view(), name='groups'),
    path('edit-user/', EditUserView.as_view(), name='edit-user'),
    path('edit-group/', EditGroupView.as_view(), name='edit-group'),
]
