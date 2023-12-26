from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,UserChangeForm
from main_app.models import Blogpost, CustomUser, Profile

class RegisterForm(UserCreationForm):
    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    user_type = forms.ChoiceField(label='Join as a:', choices=[('', '-------'),('blogger', 'Bloggers'),('viewer', 'Viewers')], widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name','email','user_type']
        label = {'first_name':'First Name','last_name':'Last Name','email':'Email'}
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={'class':'form-control'}))
    password = UsernameField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))


class PostForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = ['title', 'description','image']
        labels= {'title':'Title','description':'Description','image':'Image'}
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}), 
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address','bio','profilepic']
        labels = {'address':'Address','bio':'Bio','profilepic':'Profile Image'}
        widgets = {
            'address':forms.Textarea(attrs={'class':'form-control'}), 
            'bio':forms.Textarea(attrs={'class':'form-control'}), 
            'profilepic': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

class UserProfileUpdateForm(forms.ModelForm):
    user_type = forms.ChoiceField(
        label='Join as a:',
        choices=[('', '-------'), ('blogger', 'Bloggers'), ('viewer', 'Viewers')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'user_type']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email'}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }