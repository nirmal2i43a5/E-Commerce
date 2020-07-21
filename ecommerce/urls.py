"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Profile import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('ad3i2/', admin.site.urls),
    path('',include('Profile.urls',namespace="profile")),
    path('',include('store.urls',namespace='store')),
    path('',include('store.category_urls',namespace="category_app")),
    
      path('reset_password/',auth_views.PasswordResetView.as_view(template_name = 'passwordreset/password_reset_email.html'), 
         name = "password_reset"),
    
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name = 'passwordreset/password_reset_sent.html'), 
         name = "password_reset_done"),
    
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='passwordreset/password_reset_form.html'),
         name="password_reset_confirm"),  
       
     #<token> check  for valid user or not--><uidb64> user id encoded in base 64--this email is sent to the user
     #<uidb64> helps to know user who request for password
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='passwordreset/password_reset_complete.html'),
         name="password_reset_complete"),
  
    
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
