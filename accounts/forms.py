from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        # 親クラスの__init__メソッドを実行
        super().__init__(*args, **kwargs)
        # htmlのクラス属性を指定
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ("username", "password1", "password2",)

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # htmlのクラス属性を指定
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'