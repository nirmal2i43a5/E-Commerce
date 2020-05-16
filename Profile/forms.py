from django import forms
from store.models import Customer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm,AuthenticationForm

from django.forms import EmailField,TextInput,PasswordInput


from django.utils.translation import ugettext_lazy as _ #for protected-


class CustomerLoginForm(AuthenticationForm):
    email = EmailField(label=_("Email"), required=True,help_text=_("Required.")) #Email address is protected
    
    #i dont need to use username and password field as it is autogenerates

class SignUpForm(UserCreationForm):
   
    username=forms.CharField(widget=forms.TextInput(attrs={"placeholder": " Enter Username",}))
    email=forms.CharField(widget=forms.TextInput(attrs={"placeholder": " Enter Email",}))
    password1=forms.CharField(widget=forms.TextInput(attrs={"placeholder": " Enter Password",'type' : 'password'}),label=_("Password"))
    password2=forms.CharField(widget=forms.TextInput(attrs={"placeholder": " Confirm Password",'type' : 'password'}),label=_("Confirm Password"))
    

    
    
    # email = EmailField(label=_("Email"),required=True) #before i write this Email address bhanera show garxa.so,Email label garkao
    #Email address is protected

    
    class Meta:
        model = User
        

        fields = ('username','email','password1','password2')#'__all__' also
     
        
        #help_text will remove the default text in signup page
        help_texts= {
            'username':None,
            # 'email':"Your email should contain @" if i add email and wants help_texts for that
           #to remove help text of password and password2 go to UserCreationForm  and comment help_text in 
        }
        
  
   
   