from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password_confirmation = forms.CharField(min_length=8, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'age', 'password', 'password_confirmation')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('User already exists')
        return username

    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        password_confirmation = data.pop('password_confirmation')
        if password != password_confirmation:
            raise forms.ValidationError('Password don\'t match')
        return data

    def save(self, commit=True):
        user = User.objects.create(**self.cleaned_data)
        return user
