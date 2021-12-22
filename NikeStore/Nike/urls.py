"""NikeStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name ="index"),
    path('men/', showMen, name = "men"),
    path('women/', showWomen, name = "women"),
    path('contacts/', showContacts, name = "contacts"),
    path('showBasket/',showBasket, name = "basket"),
    path('login/', loginUser,name='loginUser'),
    path('signup/',signUpUser, name='signUpUser'),
    path('logout/',logoutUser, name='logoutUser'),
    path('adminPanel/', showAdminPanel, name = "adminPanel"),
    path('adminShoes/', showAdminShoes),
    path('adminPanel/createShoe', showAdminCreateShoe, name='createShoe'),
    path('adminPanel/deleteShoe', deleteShoeById),
    path('adminPanel/editShoe', editShoe, name='editShoe'),
    path('adminUsers/',showUsers),
    path('adminSizes/',showSizes),
    path('adminPanel/createSize/', showAdminCreateSize,name='createSize'),
    path('adminPanel/deleteSize/', deleteSizeById),
    path('adminPanel/editSize',editSize,name='editSize'),
    path('submitContact/', submitContact, name='submitContact'),
    path('adminContacts/',showAdminContacts),
    path('adminPanel/deleteContact/',deleteContact),
    path('addBasketShoe/', addBasketShoe,name='addBasketShoe'),
    path('adminOrders/', showAdminOrders),
    path('adminPanel/detailsOrder/',showDetails),
    path('clearAll/', clearAll, name = 'clearBasket'),
    path('makePurchase/',makePurchase,name='makePurchase'),
    path('details/',showShoeDetails),
]

