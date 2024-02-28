from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home-page"),
    path('products/',product,name="product-page"),
    path('chairs/',chair,name="chair-page"),
    path('tables/',table,name="table-page"),
    path('beds/',bed,name="bed-page"),
    path('sofas/',sofa,name="sofa-page"),
    path('cupboards/',cupboard,name="cupboard-page"),
    path('login/',loginUser,name="login-page"),
    path('logout/',logoutUser,name="logout-page"),
    path('signup/',signUpUser,name="signup-page"),
    path('cart/',cart,name="cart-page"),
    path('wishlist/',wishlist,name="wishlist-page"),
    path('about/',about,name="about-page"),
    path('feedback/',feedBack,name="feedback-page"),
    path('contact/',contact,name="contact-page"),
]
