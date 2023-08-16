
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserBaseForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'
        
class UserCreateForm(UserBaseForm):
    password2 = forms.CharField(widget = forms.PasswordInput())
    class Meta(UserBaseForm.Meta):
        fields = [ 'username', 'email', 'password' ]

# 회원가입 폼
class CustomSignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'signup__form-username',
        'placeholder': '아이디를 입력해주세요.',
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'signup__form-pw',
        'placeholder': '6~8자리의 영문, 숫자가 포함된 비밀번호를 입력해주세요.',
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'signup__form-pw2',
        'placeholder': '비밀번호를 다시 입력해주세요.',
    }))
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'email']
        
# 로그인 폼
class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update({
            'class': 'login__form-username',
            'placeholder': 'Username',
        })
        self.fields['password'].widget.attrs.update({
            'class': 'login__form-pw',
            'placeholder': 'Password',
        })