from django.db import models
from django.contrib.auth.models import AbstractUser


class Entity(models.Model):
    entityID = models.AutoField(primary_key=True)


class Photograph(Entity):
    dataTaken = models.DateTimeField(null=True, blank=True, auto_now=False, auto_now_add=False)
    placeTaken = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    imagePath = models.TextField(null=False, blank=False)


class Address(Entity):
    address1 = models.TextField(null=False, blank=False)
    address2 = models.TextField(null=True, blank=True)
    city = models.TextField(null=False, blank=False)
    state = models.TextField(null=False, blank=False)
    zip = models.IntegerField(null=False, blank=False)
    email = models.EmailField(max_length=100)


class User(AbstractUser):
    phone = models.TextField(null=True, blank=True)
    requiresReset = models.BooleanField(default=False)
    organizationType = models.TextField(null=True, blank=True)
    emergencyContact = models.TextField(null=True, blank=True)
    emergencyPhone = models.TextField(null=True, blank=True)
    emergencyContactRelationship = models.TextField(null=True, blank=True)
    creationDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    securityQuestion = models.TextField(null=True, blank=True)
    securityAnswer = models.TextField(null=True, blank=True)
    agentHireDate = models.DateTimeField(null=True, blank=True, auto_now=False, auto_now_add=False)
    address = models.ForeignKey(Address)
    photograph = models.ForeignKey(Photograph)


class Area(Entity):
    name = models.TextField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    placeNumber = models.IntegerField(null=False, blank=False)
    coordinatingAgent = models.ForeignKey(User, related_name='coordinating')
    supervisingAgent = models.ForeignKey(User, related_name='supervising')
    event = models.ForeignKey('Event')


class AreaSaleItem(Entity):
    name = models.TextField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    lowPrice = models.DecimalField(max_digits=10, decimal_places=2)
    highPrice = models.DecimalField(max_digits=10, decimal_places=2)
    area = models.ForeignKey(Area)
    photograph = models.ForeignKey(Photograph)


class Event(Entity):
    name = models.TextField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    startDate = models.DateTimeField(null=False, blank=False, auto_now=False, auto_now_add=False)
    endDate = models.DateTimeField(null=False, blank=False, auto_now=False, auto_now_add=False)
    mapFileName = models.TextField(null=True, blank=True)
    venueName = models.TextField(null=False, blank=False)
    address = models.ForeignKey(Address)


class Role(Entity):
    user = models.ForeignKey(User)
    area = models.ForeignKey(Area)
    name = models.TextField(null=False, blank=False)
    type = models.TextField(null=True, blank=True)
    historicalFigure = models.ForeignKey('HistoricalFigure')


class HistoricalFigure(Entity):
    name = models.TextField(null=False, blank=False)
    birthDate = models.DateField(null=False, blank=False, auto_now=False, auto_now_add=False)
    birthPlace = models.TextField(null=False, blank=False)
    deathDate = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    deathPlace = models.TextField(null=True, blank=True)
    biographicalNote = models.TextField(null=True, blank=True)
    isFictional = models.BooleanField(default=False)


class Category(Entity):
    description = models.TextField(null=False, blank=False)


class ItemSpecifications(Entity):
    name = models.TextField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    manufacturer = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User)
    photograph = models.ForeignKey(Photograph)
    category = models.ForeignKey(Category)


class Item(Entity):
    forSale = models.BooleanField(default=False)
    quantityOnHand = models.IntegerField(null=False, blank=False)
    cost = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    itemSpecifications = models.ForeignKey(ItemSpecifications)


class SerializedItem(Item):
    serialNumber = models.TextField(null=False, blank=False)
    dateIn = models.DateTimeField(null=False, blank=False, auto_now=False, auto_now_add=False)
    conditionNew = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)


class WardrobeItem(SerializedItem):
    size = models.IntegerField(null=False, blank=False)
    sizeModifier = models.IntegerField(null=True, blank=True)
    gender = models.TextField(null=True, blank=True)
    color = models.TextField(null=True, blank=True)
    pattern = models.TextField(null=True, blank=True)
    startYear = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    endYear = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    note = models.TextField(null=True, blank=True)


class RentalItem(WardrobeItem):
    timesRented = models.IntegerField(null=False, blank=False)
    dailyPrice = models.DecimalField(null=False, blank=False, max_digits=10, decimal_places=2)


class LineItem(Entity):
    transaction = models.ForeignKey('Transaction')


class SaleItem(LineItem):
    quantity = models.IntegerField(null=False, blank=False)
    item = models.ForeignKey(Item)


class Rental(LineItem):
    rentalTime = models.DateTimeField(null=False, blank=False, auto_now=False, auto_now_add=True)
    dueDate = models.DateTimeField(null=False, blank=False, auto_now=False, auto_now_add=False)
    returnTime = models.DateTimeField(null=True, blank=True, auto_now=False, auto_now_add=False)
    discountPercent = models.DecimalField(max_digits=2, decimal_places=2)
    rentalItem = models.ForeignKey(RentalItem)


class Return(LineItem):
    feeWaived = models.BooleanField(default=False)


class LateFee(Return):
    daysLate = models.IntegerField(null=False, blank=False)


class DamageFee(Return):
    description = models.TextField(null=False, blank=False)


class ShoppingCart(Entity):
    user = models.ForeignKey(User)


class CartItem(Entity):
    shoppingCart = models.ForeignKey(ShoppingCart)
    item = models.ForeignKey(Item)


class Transaction(Entity):
    orderDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    phone = models.TextField(null=True, blank=True)
    datePacked = models.DateTimeField(auto_now=False, auto_now_add=False)
    datePaid = models.DateTimeField(auto_now=False, auto_now_add=False)
    dateShipped = models.DateTimeField(auto_now=False, auto_now_add=False)
    trackingNumber = models.IntegerField(null=True, blank=True)
    placedBy = models.ForeignKey(User, related_name='placedBy')
    handledBy = models.ForeignKey(User, related_name='handledBy')
    shippingAddress = models.ForeignKey(Address)