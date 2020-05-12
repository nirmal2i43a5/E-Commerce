from django.urls import path
from store import category_views

app_name = 'category_app'

urlpatterns = [
    path('Mens_shoes_and_clothing/',category_views.Mens_shoes_and_clothing,name="Mens_shoes_and_clothing"),
]
