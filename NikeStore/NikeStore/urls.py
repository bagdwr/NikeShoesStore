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
import Nike.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Nike.views.index),
    path('men/', Nike.views.showMen),
    path('women/', Nike.views.showWomen),
    path('contacts/', Nike.views.showContacts),
    path('showBasket/',Nike.views.showBasket),
    path('login/', Nike.views.loginUser,name='loginUser'),
    path('signup/',Nike.views.signUpUser, name='signUpUser'),
    path('logout/',Nike.views.logoutUser, name='logoutUser'),
    path('adminPanel/', Nike.views.showAdminPanel),
    path('adminShoes/', Nike.views.showAdminShoes),
    path('adminPanel/createShoe', Nike.views.showAdminCreateShoe, name='createShoe'),
    path('adminPanel/deleteShoe', Nike.views.deleteShoeById),
    path('adminPanel/editShoe', Nike.views.editShoe, name='editShoe'),
    path('adminUsers/',Nike.views.showUsers),
    path('adminSizes/',Nike.views.showSizes),
    path('adminPanel/createSize/', Nike.views.showAdminCreateSize,name='createSize'),
    path('adminPanel/deleteSize/', Nike.views.deleteSizeById),
    path('adminPanel/editSize',Nike.views.editSize,name='editSize'),
    path('submitContact/', Nike.views.submitContact, name='submitContact'),
    path('adminContacts/',Nike.views.showAdminContacts),
    path('adminPanel/deleteContact/',Nike.views.deleteContact),
    path('addBasketShoe/', Nike.views.addBasketShoe,name='addBasketShoe'),
    path('adminOrders/', Nike.views.showAdminOrders),
    path('adminPanel/detailsOrder/',Nike.views.showDetails),
    path('clearAll/', Nike.views.clearAll),
    path('makePurchase/',Nike.views.makePurchase,name='makePurchase'),
    path('details/',Nike.views.showShoeDetails),
]

