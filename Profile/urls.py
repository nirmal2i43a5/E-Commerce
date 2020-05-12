from django.urls import path
from Profile import views

app_name = "dashboard"
urlpatterns = [
    path('',views.dashboard,name="dashboard"),
    
]
