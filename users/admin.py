from django.contrib import admin

from users.models import Group, User


# Register your models here.
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    fields = ('name', 'description')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'group', 'created')
    readonly_fields = ('created',)

