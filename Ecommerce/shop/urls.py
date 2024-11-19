"""
URL configuration for Ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from shop import views
app_name="shop"
urlpatterns = [

    path('', views.categories, name="categories"),
    path('products/<int:p>',views.products,name="products"),
    path('details_products/<int:p>',views.details_products,name="details_products"),
    path('register/',views.register, name="register"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),
    path('addcat',views.add_categories,name="addcat"),
    path('addpro',views.add_products,name="addpro"),
    path('addstock/<int:p>',views.addstock,name="addstock"),
]
