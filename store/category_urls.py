from django.urls import path
from store import category_views

app_name = 'category_app'

urlpatterns = [
    path('mens_items/',category_views.mens_items,name="mens_items"),
    path('womens_items/',category_views.womens_items,name="womens_items"),
    path('laptops/',category_views.laptops,name="laptops"),
    path('mobiles/',category_views.mobiles,name="mobiles"),
    path('cameras/',category_views.cameras,name="cameras"),
    path('search-camera/',category_views.search_cameras,name="search"),
]
