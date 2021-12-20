from Nike.models import *
from Nike.Classes import *

def getAllMenShoes():
    shoes=Shoe.objects.filter(genderId=1)
    returnShoes=list()
    for shoe in shoes:
        sizes=getShoeSizes(shoe.id)
        returnSize=list()
        for size in sizes:
            tempSize=SizeLocal(size.id,size.sizeNumb,size.sizeAmount)
            returnSize.append(tempSize)
        tempShoe=ShoeLocal(shoe.id, shoe.name, shoe.price,1, shoe.image,shoe.description,shoe.color, returnSize)
        returnShoes.append(tempShoe)
    return returnShoes

def getShoeSizes(id):
    return Size.objects.filter(shoeId=id).order_by('sizeNumb')

def getAllWomenShoes():
    shoes=Shoe.objects.filter(genderId=2)
    returnShoes=list()
    for shoe in shoes:
        sizes=getShoeSizes(shoe.id)
        returnSize=list()
        for size in sizes:
            tempSize=SizeLocal(size.id,size.sizeNumb,size.sizeAmount)
            returnSize.append(tempSize)
        tempShoe=ShoeLocal(shoe.id, shoe.name, shoe.price,2, shoe.image, shoe.description, shoe.color, returnSize)
        returnShoes.append(tempShoe)
    return returnShoes

def getGenderById(id):
    return Gender.objects.filter(id=id).first()

def createShoe(request):
    Shoe.objects.create(name=request.POST['name'], genderId=getGenderById(request.POST['genderId']), price=request.POST['price'],image=request.FILES.get('shoePicture','shoes/default.png'), description=request.POST['description'], color=request.POST['color'])
    return True

def deleteShoe(request):
    Size.objects.filter(shoeId=request.GET['id']).delete()
    Shoe.objects.filter(id=request.GET['id']).delete()
    return True

def getShoeById(shoeId):
    return Shoe.objects.filter(id=shoeId).first()

def getShoeLocalById(shoeId):
    shoe=Shoe.objects.filter(id=shoeId).first()
    shoeLocal=ShoeLocal(shoe.id,shoe.name,shoe.price,shoe.genderId, shoe.image,shoe.description,shoe.color,getShoeSizes(shoe.id))
    return shoeLocal

def updateShoe(request):
    shoe=getShoeById(request.POST['id'])
    shoe.name=request.POST['name']
    shoe.price=request.POST['price']
    shoe.genderId=getGenderById(request.POST['genderId'])
    shoe.color=request.POST['color']
    shoe.description=request.POST['description']
    shoe.image=request.FILES.get('shoePicture','shoes/default.png')
    shoe.save()
    return True

def getAllUsers():
    return User.objects.all()

def getAllSizes():
    return Size.objects.all()

def createSize(request):
    Size.objects.create(sizeNumb=request.POST['sizeNumb'],sizeAmount=request.POST['sizeAmount'],shoeId=getShoeById(request.POST['shoe_id']))
    return True

def deleteSize(request):
    Size.objects.filter(id=request.GET['id']).delete()
    return True

def getSizeById(id):
    return Size.objects.filter(id=id).first()

def updateSize(request):
    size=Size.objects.filter(id=request.POST['id']).first()
    size.sizeNumb=request.POST['sizeNumb']
    size.sizeAmount=request.POST['sizeAmount']
    size.shoeId=getShoeById(request.POST['shoe_id'])
    size.save()
    return True

def createContact(request):
    Contact.objects.create(contactName=request.POST['name'], contactEmail=request.POST['email'], contactSubject=request.POST['subject'],
                           contactMessage=request.POST['message'], userId=request.user)
    return True

def getAllContacts():
    return Contact.objects.all()

def deleteContactById(request):
    Contact.objects.filter(id=request.GET['id']).delete()
    return True

def createOrder(request, shoes):
    orderNumb=len(Order.objects.all())+1
    Order.objects.create(userId=request.user,orderNumber=orderNumb)
    for shoe in shoes:
        OrderShoe.objects.create(orderNumber=orderNumb,shoeId_id=shoe.id,sizeId_id=shoe.sizes.id)
    return True

def getAllOrders():
    return Order.objects.all()

def getOrderShoe(orderNumb):
    return OrderShoe.objects.filter(orderNumber=orderNumb)
