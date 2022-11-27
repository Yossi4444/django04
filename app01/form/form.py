from app01 import models
from django.core.validators import RegexValidator
from django import forms
from django.core.validators import ValidationError
from app01.utils.encrypt import md5

class UserModelForm(forms.ModelForm):
    name= forms.CharField(min_length=2,label='姓名')
    class Meta:
        model=models.UserInfo
        fields = ['name','gender','age','password','account','create_time','depart']
        # 添加属性：
        # 方式一
        # widgets = {
        #     'name':forms.TextInput(attrs={'class':'form-control'}),
        #     'gender': forms.TextInput(attrs={'class': 'form-control'}),
        #     'age': forms.TextInput(attrs={'class': 'form-control'}),
        #     'password': forms.TextInput(attrs={'class': 'form-control'}),
        #     'account': forms.TextInput(attrs={'class': 'form-control'}),
        #     'create_time':forms.TextInput(attrs={'class':'form-control'}),
        #     'depart': forms.TextInput(attrs={'class': 'form-control'}),
        # }
        # 方式二
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs={'class':'form-control'}
class PrettyNumModelForm(forms.ModelForm):
    # 验证：方式一
    mobile = forms.CharField(
        label = '电话',
        validators=[RegexValidator(r'^1[3-9]\d{9}$','手机号格式错误')],
        # disabled=True
    )
    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']
        # 添加属性：
        # 方式一
        # widgets = {
        #     'mobile':forms.TextInput(attrs={'class':'form-control'}),
        #     'price': forms.TextInput(attrs={'class': 'form-control'}),
        #     'level': forms.Select(attrs={'class': 'form-control'}),
        #     'status': forms.Select(attrs={'class': 'form-control'}),
        # }
        # 验证：方式二
        # def clean_mobile(self):
        #     txt_mobile = self.clean_mobile['mobile']
        #     exists = models.PrettyNum.objects.filter(mobile=txt_mobile).exists()
        #     if exists:
        #         raise ValidationError('电话已存在')
        #     if len(txt_mobile) != 11:
        #         raise ValidationError('格式错误')
        #     return txt_mobile
        # 添加属性：方式二：
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs={'class':'form-control'}
class PrettyNumEditModelForm(forms.ModelForm):
    # 验证：方式一
    mobile = forms.CharField(
        label = '电话',
        # disabled=True
        validators=[RegexValidator(r'^1[3-9]\d{9}$','手机号格式错误')],
    )
    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']
        # 添加属性：
        # 方式一
        # widgets = {
        #     'mobile':forms.TextInput(attrs={'class':'form-control'}),
        #     'price': forms.TextInput(attrs={'class': 'form-control'}),
        #     'level': forms.Select(attrs={'class': 'form-control'}),
        #     'status': forms.Select(attrs={'class': 'form-control'}),
        # }
        # 验证：方式二(不能手机号重复检测)
        # def clean_mobile(self):
        #     txt_mobile = self.cleaned_data['mobile']
        #     exists = models.PrettyNum.objects.filter(mobile=txt_mobile).exists()
        #     if exists:
        #         raise ValidationError('电话已存在')
        #     if len(txt_mobile) != 11:
        #         raise ValidationError('格式错误')
        #     return txt_mobile
        # 添加属性：方式二：
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs={'class':'form-control'}
class AdminModelForm(forms.ModelForm):
    confirm_password = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput(render_value=True)
    )
    class Meta:
        model = models.Admin
        fields = {'name','password','confirm_password'}
        widgets = {
            'password':forms.PasswordInput(render_value=True)
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control'}

    def clean_password(self):
       password = self.cleaned_data.get('password')
       password = md5(password)
       return password

    def clean_confirm_password(self):
       password = self.cleaned_data.get('password')
       confirm_password = self.cleaned_data.get('confirm_password')
       confirm_password=md5(confirm_password)
       if confirm_password != password:
           raise ValidationError('密码不一致')
       return confirm_password

class AdminEditModelForm(forms.ModelForm):
    class Meta:
        model = models.Admin
        fields = {'name'}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control'}
class LoginFrom(forms.Form):
    name = forms.CharField(
        label='用户名',
        widget = forms.TextInput
    )
    password = forms.CharField(
        label='密码',
        widget = forms.PasswordInput
    )
    code = forms.CharField(
        label='验证码',
        widget=forms.TextInput
    )
    def clean_password(self):
        password = self.cleaned_data.get('password')
        return md5(password)
        #return password