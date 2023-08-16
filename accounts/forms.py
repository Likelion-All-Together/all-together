
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
class SignUpForm(UserCreationForm):
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
        
    # username = forms.CharField(
    #     label='<label class="your-label-class"><img src="{% static "image/user.svg" %}" alt="Username Image"></label>',
    #     widget=forms.TextInput(attrs={'class': 'your-label-class'}),
    # )
    
    # password = forms.CharField(
    #     label='<label class="your-password-label-class"><img src="{% static "image/password.svg" %}" alt="Password Image"></label>',
    #     widget=forms.PasswordInput(attrs={'class': 'your-password-class'}),
    # )
