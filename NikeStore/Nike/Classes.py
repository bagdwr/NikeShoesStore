class ShoeLocal:
    def __init__(self,id,name,price,genderId,image_url,description,color,sizes):
        self.id=id
        self.name=name
        self.price=price
        self.genderId=genderId
        self.image_url=image_url
        self.description=description
        self.color=color
        self.sizes=sizes

class SizeLocal:
    def __init__(self,id,sizeNumber,sizeAmount):
        self.id=id
        self.sizeNumber=sizeNumber
        self.sizeAmount=sizeAmount

class OrderLocal:
    def __init__(self,id, orderNumber,orderUser,shoes, overallPrice):
        self.id=id
        self.orderNumber=orderNumber
        self.orderUser=orderUser
        self.shoes=shoes
        self.overallPrice=overallPrice