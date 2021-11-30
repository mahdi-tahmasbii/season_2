from django import forms
from .models import User
from django.core import validators


class EditUserForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام خود را وارد نمایید', 'class': 'form-control'}),
        label='Name'
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا ایمیل خود را وارد نمایید', 'class': 'form-control'}),
        label='Email'
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام خانوادگی خود را وارد نمایید', 'class': 'form-control'}),
        label='Last Name'
    )


class RegisterForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
        label='User Name',
        validators=[
            validators.MaxLengthValidator(limit_value=20,
                                          message='تعداد کاراکترهای وارد شده نمیتواند بیشتر از 20 باشد'),
            validators.MinLengthValidator(8, 'تعداد کاراکترهای وارد شده نمیتواند کمتر از 8 باشد')
        ]
    )

    email = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
        label='Email',
        validators=[
            validators.EmailValidator('')
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '', 'class': 'form-control'}),
        label='Password'
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': '', 'class': 'form-control'}),
        label='Repeat Password'
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists_user_by_email = User.objects.filter(email=email).exists()
        if is_exists_user_by_email:
            raise forms.ValidationError('')
        return email

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_exists_user_by_username = User.objects.filter(username=user_name).exists()

        if is_exists_user_by_username:
            raise forms.ValidationError('')

        return user_name

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        print(password)
        print(re_password)

        if password != re_password:
            raise forms.ValidationError('')

        return password


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')

        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['username'].help_text = None

        if not user.is_superuser:
            self.fields['username'].disabled = True
            self.fields['email'].disabled = True
            self.fields['special_user'].disabled = True
            self.fields['is_author'].disabled = True

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',
                  'special_user', 'is_author']
