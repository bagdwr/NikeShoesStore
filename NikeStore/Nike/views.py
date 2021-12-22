import django as django
from django.shortcuts import render
from .Classes import ShoeLocal
from .DBmanager import *
from .models import *

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import *
from django.contrib.auth.decorators import login_required
import json

SHOES = list()


def getOverallPrice():
    sum = 0
    for shoe in SHOES:
        sum = sum + shoe.price
    return sum


def index(request):
    return render(request, "index.html", context={'summa': getOverallPrice()})


def showMen(request):
    menShoes = getAllMenShoes()
    data_dict = {'list': menShoes, 'header': 'Men shoes', 'summa': getOverallPrice()}
    return render(request, "shoe.html", context=data_dict)


def showWomen(request):
    womenShoes = getAllWomenShoes()
    data_dict = {'list': womenShoes, 'header': 'Women shoes', 'summa': getOverallPrice()}
    return render(request, "shoe.html", context=data_dict)


def showContacts(request):
    return render(request, "contacts.html", context={'summa': getOverallPrice()})


def showBasket(request):
    return render(request, "basket.html", context={'shoes': SHOES, 'summa': getOverallPrice()})


def showShoeDetails(request):
    return render(request, "details.html",
                  context={'shoe': getShoeLocalById(request.GET['id']), 'summa': getOverallPrice()})


@csrf_exempt
def signUpUser(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm(), 'summa': getOverallPrice()})
    else:
        try:
            if User.objects.filter(username=request.POST['email']).exists() or User.objects.filter(
                    username=request.POST['email']).exists():
                return render(request, 'signup.html', {'form': UserCreationForm(), 'summa': getOverallPrice(), 'error':'there is already such email'})
            user = User.objects.create_user(username=request.POST['email'], last_name=request.POST['phone'],
                                            password=request.POST['password'], email=request.POST['email'])
            user.save()
            login(request, user)
            return redirect('/')
        except Exception as e:
            return render(request, 'signup.html', {'form': UserCreationForm()}, 'error', 'this acc - ', )


@csrf_exempt
def loginUser(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': AuthenticationForm(), 'summa': getOverallPrice()})
    else:
        user = authenticate(request, username=request.POST['email'], password=request.POST['password'])
        if user is None:
            return redirect('/login')
        else:
            login(request, user)
            return redirect('/')


def addBasketShoe(request):
    if request.method == 'POST':
        size = getSizeById(request.POST['sizeId'])
        shoe = getShoeById(request.POST['shoeId'])

        # shoes=list()
        # shoesFromSession=request.session.get('basketShoes',None)
        # if shoesFromSession is None:
        #     shoes.append(shoe)
        # else:
        #     shoes.append(shoesFromSession)
        #     shoes.append(shoe)
        # request.session['basketShoes'] = {'shoes':shoes}
        if shoe is not None and size is not None:
            shoe.sizes = size
            SHOES.append(shoe)
            print(SHOES)

        if shoe.genderId_id == 1:
            return redirect('/men')
        else:
            return redirect('/women')


# region admin
@login_required
def logoutUser(request):
    if request.method == 'GET':
        logout(request)
        return redirect('loginUser')


@login_required
def showAdminPanel(request):
    if request.user.is_superuser:
        return render(request, 'Admin_templates/adminPanel.html')
    else:
        return redirect('/')


@login_required
def showAdminShoes(request):
    if request.user.is_superuser:
        allShoes = getAllMenShoes() + getAllWomenShoes()
        return render(request, 'Admin_templates/adminShoes.html', context={'shoes': allShoes})
    else:
        return redirect('/')


@login_required
def showAdminCreateShoe(request):
    if request.method == 'GET':
        return render(request, 'Admin_templates/adminCreateShoe.html')
    if request.method == 'POST':
        if createShoe(request):
            return redirect('/adminShoes')
        return redirect('/adminPanel')


@login_required
def deleteShoeById(request):
    if request.user.is_superuser:
        if request.method == 'GET':
            if deleteShoe(request):
                return redirect('/adminShoes')
        else:
            return redirect('/adminPanel')
    else:
        return redirect('/')


@login_required
def editShoe(request):
    if request.user.is_superuser:
        if request.method == 'GET':
            return render(request, 'Admin_templates/adminEditShoe.html',
                          context={'shoe': getShoeById(request.GET['id'])})
        if request.method == 'POST':
            if updateShoe(request):
                return redirect('/adminShoes')
    else:
        return redirect('/')


@login_required
def showUsers(request):
    if request.user.is_superuser:
        return render(request, 'Admin_templates/adminUsers.html', context={'users': getAllUsers()})
    else:
        return redirect('/')


@login_required
def showSizes(request):
    if request.user.is_superuser:
        return render(request, 'Admin_templates/adminSizes.html', context={'sizes': getAllSizes()})
    else:
        return redirect('/')


@login_required
def showAdminCreateSize(request):
    if request.method == 'GET':
        return render(request, 'Admin_templates/adminCreateSize.html',
                      context={'shoes': getAllMenShoes() + getAllWomenShoes()})
    if request.method == 'POST':
        if createSize(request):
            return redirect('/adminSizes')
        return redirect('/adminPanel')


@login_required
def deleteSizeById(request):
    if request.user.is_superuser:
        if request.method == 'GET':
            if deleteSize(request):
                return redirect('/adminSizes')
        else:
            return redirect('/adminPanel')
    else:
        return redirect('/')


@login_required
def editSize(request):
    if request.user.is_superuser:
        if request.method == 'GET':
            return render(request, 'Admin_templates/adminEditSize.html',
                          context={'size': getSizeById(request.GET['id']),
                                   'shoes': getAllMenShoes() + getAllWomenShoes()})
        if request.method == 'POST':
            if updateSize(request):
                return redirect('/adminSizes')
    else:
        return redirect('/')


@login_required
def submitContact(request):
    if request.method == 'POST':
        if createContact(request):
            return redirect('/contacts')


@login_required
def showAdminContacts(request):
    if request.user.is_superuser:
        return render(request, 'Admin_templates/adminContacts.html',
                      context={'contacts': getAllContacts()})
    else:
        return redirect('/')


@login_required
def deleteContact(request):
    if request.user.is_superuser:
        if request.method == 'GET':
            if deleteContactById(request):
                return redirect('/adminContacts')
        else:
            return redirect('/adminPanel')
    else:
        return redirect('/')


# endregion

def clearAll(request):
    SHOES.clear()
    return redirect('/showBasket')


@login_required
def makePurchase(request):
    if request.method == 'POST':
        shoes = SHOES
        if createOrder(request, shoes):
            clearAll(request)
    return redirect('/')


@login_required
def showAdminOrders(request):
    if request.user.is_superuser:
        if request.method == 'GET':
            ords = getAllOrders()
            orders = list()
            for order in ords:
                orderShoes = getOrderShoe(order.orderNumber)
                shoes = list()
                for orderShoe in orderShoes:
                    shoe = getShoeById(orderShoe.shoeId_id)
                    shoes.append(ShoeLocal(shoe.id, shoe.name, shoe.price, shoe.genderId, shoe.image, shoe.description,
                                           shoe.color, getSizeById(orderShoe.sizeId_id)))
                orders.append(OrderLocal(order.id, orderNumber=order.orderNumber, shoes=shoes, orderUser=order.userId,
                                         overallPrice=getShoesOverallPrice(shoes)))
            return render(request, 'Admin_templates/adminOrders.html', context={'orders': orders})


def getShoesOverallPrice(shoes):
    sum = 0
    for shoe in shoes:
        sum = shoe.price + sum
    return sum


@login_required
def showDetails(request):
    if request.user.is_superuser:
        if request.method == 'GET':
            orderShoes = getOrderShoe(request.GET['orderNumber'])
            shoes = list()
            for orderShoe in orderShoes:
                shoe = getShoeById(orderShoe.shoeId_id)
                shoes.append(
                    ShoeLocal(shoe.id, shoe.name, shoe.price, shoe.genderId, shoe.image, shoe.description, shoe.color,
                              getSizeById(orderShoe.sizeId_id)))
            return render(request, 'Admin_templates/adminDetailsOrder.html', context={'shoes': shoes})
