
from django.urls import path


from shop.views import *

urlpatterns = [
    path('', home_page_view, name='home'),  
    path('category/<slug:category>/', home_page_view, name='category'),   
    path('shop/', shop_page_view, name='shop'),
    path('shop/shop-produit/', shop_detail_view, name='details'),
    path('shop/shop-detail/<int:pk>/', shop_detail_view, name='details'),
    path('shop/category/<slug:category>', shop_page_view, name='souscategory'),   

    path('shop/shoping-cart/', shop_cart_view, name='card'),
    path('contact/', contact_view, name='contact'),

    path('blog/', blog_view, name='blog'),
    path('blog/category/<slug:category>', blog_view, name='category'),
    path('blog/<slug:slug>', blog_detail_view, name='blog_detail'),
    
    path('checkout/', checkout_view, name='checkout'),
]
