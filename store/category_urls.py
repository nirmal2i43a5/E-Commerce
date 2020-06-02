from django.urls import path
from store import category_views
from store import category_search


app_name = 'category_app'

urlpatterns = [
    path('mens_items/',category_views.mens_items,name="mens_items"),
    path('womens_items/',category_views.womens_items,name="womens_items"),
    path('laptops/',category_views.laptops,name="laptops"),
    path('mobiles/',category_views.mobiles,name="mobiles"),
    path('cameras/',category_views.cameras,name="cameras"),
    #for search
    path('search-camera/',category_search.search_cameras,name="search-camera"),
     path('search-laptop/',category_search.search_laptops,name="search-laptop"),
      path('search-mobile/',category_search.search_mobiles,name="search-mobile"),
      path('search-women/',category_search.search_womens,name="search-women"),
       path('search-men/',category_search.search_mens,name="search-men"),
]
