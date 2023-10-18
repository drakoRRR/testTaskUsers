from django import forms

from users.models import User, Group


class AddUserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter username'
    }), required=True)
    group = forms.ModelChoiceField(queryset=Group.objects.all())

    class Meta:
        model = User
        fields = ('username', 'group')


class AddGroupForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter group name'
    }), required=True)
    description = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter group description'
    }), required=True)

    class Meta:
        model = User
        fields = ('name', 'description')
