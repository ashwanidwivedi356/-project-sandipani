from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm


from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Customer


class CustomerRegistrationForm(UserCreationForm):
    password1=forms.CharField(label='Password', widget=forms.PasswordInput
    (attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password(again)', widget=forms.PasswordInput
    (attrs={'class':'form-control'}))
    email=forms.CharField(required=True, widget=forms.EmailInput
    (attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields=['username','email','password1','password2']
        labels = {'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}

# login

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput
    (attrs={'autocomplete':'current-password','class':'form-control'}))


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"),
    strip=False, widget=forms.PasswordInput(attrs=
    {'autocomplete': 'current-password','autofocus':True,'class':'form-control'}))
    new_password1 = forms.CharField(label=_("new_password"),
    strip=False, widget=forms.PasswordInput(attrs=
    {'autocomplete': 'new-password','autofocus':True,'class':'form-control'}),
    help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("new_password"),
    strip=False, widget=forms.PasswordInput(attrs=
    {'autocomplete': 'new-password','autofocus':True,'class':'form-control'}))
    
    
   
class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254,widget=forms.EmailInput
    (attrs={'autocomplete':'email','class':'form-control'}))


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New_Password"),
    strip=False, widget=forms.PasswordInput(attrs=
    {'autocomplete': 'new-password','class':'form-control'}),
    help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("ConfirmNew_Password"),
    strip=False, widget=forms.PasswordInput(attrs=
    {'autocomplete': 'new-password','class':'form-control'}))
    
    

    
# Modelform

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','locality','city','state','zipcode']
        widgets={'name': forms.TextInput(attrs=
        {'class':'form-control'}), 'locality': forms.TextInput(attrs=
        {'class':'form-control'}), 'city':forms.TextInput(attrs=
        {'class':'form-control'}),
        'state':forms.Select(attrs={'class':'form-control'}),
        'zipcode':forms.NumberInput(attrs={'class':'form-control'})}


# contact page
class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50, label="First Name")
    last_name = forms.CharField(max_length=50, label="Last Name")
    email = forms.EmailField(label="Email Address")
    # email=ashwanidwivedi076@gmail.com
    country = forms.CharField(max_length=100, label="Country")
    category = forms.ChoiceField(
        choices=[
            ('general', 'General Inquiry'),
            ('support', 'Support'),
            ('feedback', 'Feedback')
        ],
        label="Category"
    )
    subject = forms.CharField(max_length=100, label="Subject")
    message = forms.CharField(widget=forms.Textarea, label="Message")

# saved database

# from django import forms
# from .models import ContactMessage

# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = ContactMessage
#         fields = ['first_name', 'last_name', 'email', 'country', 'category', 'subject', 'message']

# pandit

from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['address', 'anusthan', 'pandit_details', 'booking_date']
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
        }
