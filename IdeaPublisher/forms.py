from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from captcha.fields import ReCaptchaField
from django import forms

from IdeaPublisher.models import Feedback, Idea
from django.forms.widgets import PasswordInput, TextInput
from simplemathcaptcha.fields import MathCaptchaField
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, Layout, Div, Field, Fieldset, Hidden
from crispy_forms.bootstrap import (FormActions, PrependedText, PrependedAppendedText)

class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            )
        exclude = ('password',)           
    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Field('username',css_class='span2'),
            Field('first_name',css_class='span2'),
            Field('last_name',css_class='span2'),
            Field('email',css_class='span2'),
             FormActions
            (
                Submit('login', 'Save changes',css_class='span2'),
            )
            )
    def clean_password(self):
        return ""


class MyAuthenticationForm(AuthenticationForm):
    # add your form widget here
    #captcha = ReCaptchaField(label="I'm a human",attrs={'theme' : 'clean','id' : 'alain'})
    #widget = forms.TextInput(attrs={'placeholder': 'username'})
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'type a valid username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'type a valid password'}))
    captcha = MathCaptchaField(label="Are you a human?")
    def __init__(self, *args, **kwargs):
        super(MyAuthenticationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        #self.helper.label_class = 'col-xs-6 col-md-6 col-lg-6'
        #self.helper.field_class = 'col-xs-6 col-md-6 col-lg-6'
        self.helper.layout = Layout(
            Field('username',css_class='span2'),
            Field('password',css_class='span2'),
            Field('captcha',css_class='span2'),
             FormActions
            (
                Submit('login', 'Login',css_class='span2'),
                HTML("""<input id="register" class="btn btn-primary btn-large" type="button" onclick="location.href='../newUser/';" name="button" value="Register" />"""),
                Hidden('next', '/IdeaPublisher/')
            )
            )        
        

from django_password_strength.widgets import PasswordStrengthInput, PasswordConfirmationInput
class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    password1 = forms.CharField(label="Password", widget=PasswordStrengthInput())
    password2 = forms.CharField(label="Password confirmation", widget=PasswordConfirmationInput())
    captcha = MathCaptchaField(label="Are you a human?")

    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'username', 'email', 'password1', 'password2')

    def save(self, commit = True):
        user = super(UserCreationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()

        return user
    def __init__(self, *args, **kwargs):
        super(MyRegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        #self.helper.label_class = 'col-xs-4 col-md-4 col-lg-4'
        #self.helper.field_class = 'col-xs-8 col-md-8 col-lg-8'
        self.helper.layout = Layout(
            Field('last_name',css_class='span2'),
            Field('first_name',css_class='span2'),
            Field('username',css_class='span2'),
            Field('email',css_class='span2'),
            Field('password1',css_class='span2'),
            Field('password2',css_class='span2'),
            Field('captcha',css_class='span2'),
             FormActions
            (
                #HTML("""<input id="register" type="button" onclick="location.href='../newUser/';" name="button" value="Register" />"""),
                Submit('register', 'Register',css_class='span2'),
            )
            )            

class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        exclude = ('update_count',)
    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-xs-4 col-md-4 col-lg-4'
        self.helper.field_class = 'col-xs-8 col-md-8 col-lg-8'
        self.helper.form_method = 'post'

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        widgets = {'descripcion': forms.Textarea(attrs={'rows':4}),'project': forms.Textarea(attrs={'rows':6}),'owner': forms.HiddenInput()}
    def __init__(self,user_as_owner, *args, **kwargs):
        super(IdeaForm, self).__init__(*args, **kwargs)
        self.fields['owner'].initial = user_as_owner
		
class IdeaUpdateForm(forms.ModelForm):
    class Meta:
        model = Idea
        exclude = ('owner',)
        widgets = {'descripcion': forms.Textarea(attrs={'rows':4}), 'project': forms.Textarea(attrs={'rows':6})}
		
class ExampleForm(PasswordChangeForm):
    old_password = forms.CharField(label='Previous password:',widget=PasswordInput())
    new_password1 = forms.CharField(label='New password:',widget=PasswordStrengthInput())
    new_password2 = forms.CharField(label='Confirm new password:',widget=PasswordConfirmationInput())
    def __init__(self, *args, **kwargs):
        super(ExampleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('old_password',css_class='span2'),
            Field('new_password1',css_class='span2'),
            Field('new_password2',css_class='span2'),
            FormActions
            (
                Submit('change', 'Salvar mi nueva clave',css_class='span2'),
            )
        )		