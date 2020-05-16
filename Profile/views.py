from django.shortcuts import render,redirect

# from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import CreateView
from Profile.forms import CustomerLoginForm,SignUpForm

# Create your views here.Perfect
def dashboard(request):
	return render(request,'profile/dashboard.html')

class CustomerLoginForm(LoginView):
	template_name = 'profile/login.html'
	form_class = CustomerLoginForm
	

	
	def get_success_url(self):#default
		
		if self.request.user.is_superuser:
			return '/admin/'
		
		return '/store'
	
	
class SignUpView(CreateView):
	template_name = 'profile/signup.html'
	form_class = SignUpForm
	
	def form_valid(self,form):
		# email = form.cleaned_data.get('email') #for extra attribite
		# contact = form.cleaned_data.get('contact')
		#various sms and others
		form.save()
		# user = form.cleaned_data.get('username')
		# messages.add_message(self.request, messages.INFO, ' Account successfully register for ' +user)
		return redirect('dashboard:login')

class Logout(LogoutView):
    pass


