from django.urls import path
from Profile import views
from django.contrib.auth import views as auth_views
app_name = "dashboard"
urlpatterns = [
    path('',views.dashboard,name="dashboard"),
    path('login/',views.CustomerLoginForm.as_view(),name="login"),
    path('signup/',views.SignUpView.as_view(),name="signup"),
    path('logout/',views.Logout.as_view(),name="logout"),
    
]
