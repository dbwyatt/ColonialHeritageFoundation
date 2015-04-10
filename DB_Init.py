#!/usr/bin/env python3

# this if for the new models file
# put this in the top level folder in the project same place as manage.py
# run it with the command: python DB_init.py
# python3 DB_Init.py  for nick

import os
import sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'ColonialHeritageFoundation.settings'
import django
django.setup()

import homepage.models as hmod
from django.contrib.auth.models import Group, Permission, ContentType
from django.db import connection
import subprocess
# #### DROP DATABASE, RECREATE IT, THEN MIGRATE IT #################

cursor = connection.cursor()
cursor.execute("DROP SCHEMA PUBLIC CASCADE")
cursor.execute("CREATE SCHEMA PUBLIC")
subprocess.call([sys.executable, "manage.py", "migrate"])

print('Database Migrated')

# #### CREATE PERMISSIONS/GROUPS #####################
Permission.objects.all().delete()
Group.objects.all().delete()

permissionU = Permission()
permissionU.codename = 'User'
permissionU.content_type = ContentType.objects.get(id=9)
permissionU.name = 'user'
permissionU.save()
User = Group()
User.name = "User"
User.save()
User.permissions.add(permissionU)

permissionM = Permission()
permissionM.codename = 'Manager'
permissionM.content_type = ContentType.objects.get(id=8)
permissionM.name = 'manager'
permissionM.save()
Manager = Group()
Manager.name = "Manager"
Manager.save()
Manager.permissions.add(permissionM, permissionU)

permissionA = Permission()
permissionA.codename = 'Admin'
permissionA.content_type = ContentType.objects.get(id=7)
permissionA.name = 'admin'
permissionA.save()
Admin = Group()
Admin.name = "Admin"
Admin.save()
Admin.permissions.add(permissionA, permissionM, permissionU)

# To add all permissions to a group (Admin in this case)
# permissions = Permission.objects.all()
# for x in permissions:
#     Admin.permissions.add(x)

print('Permissions Initialized')


# ########### MAKE USERS ####################

# create a photograph and adress and let the users point to it
photograph = hmod.Photograph()
photograph.imagePath = '1.gif'
photograph.save()

address = hmod.Address()
address.address1 = '790'
address.address2 = 'TNRB'
address.city = 'Provo'
address.state = 'UT'
address.zip = '84604'
address.email = 'address'
address.save()


hmod.User.objects.all().delete()
user = hmod.User()
user.username = 'ryguy'
user.last_name = "Evans"
user.first_name = "Ryan"
user.email = 'ryguy@gmail.com'
user.security_question = "School?"
user.security_answers = "BYU"
user.set_password('5000336')
user.is_superuser = True
user.address = address
user.photograph = photograph
user.save()
user.groups.add(Admin)

user = hmod.User()
user.username = 'dbwyatt'
user.last_name = "Wyatt"
user.first_name = "Daniel"
user.email = 'dw@gmail.com'
user.security_question = "School?"
user.security_answers = "BYU"
user.set_password('happy')
user.is_superuser = True
user.address = address
user.photograph = photograph
user.save()
user.groups.add(Admin)

user = hmod.User()
user.username = 'NickSucks'
user.last_name = "Stevens"
user.first_name = "Nick"
user.email = 'NS@gmail.com'
user.security_question = "School?"
user.security_answers = "BYU"
user.set_password('ilikeadodadjango')
user.is_superuser = False
user.address = address
user.photograph = photograph
user.save()
user.groups.add(User)

print('Useres Created')

# ########### Fill Models ####################

address = hmod.Address()
address.address1 = '600 S State St.'
address.address2 = 'TNRB'
address.city = 'Orem'
address.state = 'UT'
address.zip = '84058'
address.email = 'address'
address.save()

event = hmod.Event()
event.name = 'Heritage Festival'
event.description = 'The big heritage festival. Where tons of people dress up and do colonial stuff'
event.startDate = '2015-07-03 12:01'
event.endDate = '2015-07-05 12:02'
event.mapFileName = 'a map here?'
event.venueName = 'Scera Park'
event.address = address
event.save()


area = hmod.Area()
area.name = 'Bakery'
area.description = 'An old fasioned brick oven, bread is always for sale'
area.placeNumber = '1'
area.coordinatingAgent = user
area.supervisingAgent = user
area.event = event
area.save()

area = hmod.Area()
area.name = 'Black Smith'
area.description = 'Hourly demonstrations of horseshoe making.'
area.placeNumber = '2'
area.coordinatingAgent = user
area.supervisingAgent = user
area.event = event
area.save()

area = hmod.Area()
area.name = 'Basketry'
area.description = 'Basking making activities for all ages and fancy baskets for sale'
area.placeNumber = '3'
area.coordinatingAgent = user
area.supervisingAgent = user
area.event = event
area.save()


photograph = hmod.Photograph()
photograph.imagePath = 'smallbasket.gif'
photograph.save()

areaItem = hmod.AreaSaleItem()
areaItem.name = 'Small Baskets'
areaItem.description = 'small handmade baskets of varying color'
areaItem.lowPrice = 5.00
areaItem.highPrice = 10.00
areaItem.area = area
areaItem.photograph = photograph
areaItem.save()


photograph = hmod.Photograph()
photograph.imagePath = 'largebasket.jpg'
photograph.save()

areaItem = hmod.AreaSaleItem()
areaItem.name = 'Large Baskets'
areaItem.description = 'large handmade baskets of varying color'
areaItem.lowPrice = 10.00
areaItem.highPrice = 30.00
areaItem.area = area
areaItem.photograph = photograph
areaItem.save()

photograph = hmod.Photograph()
photograph.imagePath = 'otherbasket.jpg'
photograph.save()

areaItem = hmod.AreaSaleItem()
areaItem.name = 'Make yourself Baskets'
areaItem.description = 'make your own basket'
areaItem.lowPrice = 5.00
areaItem.highPrice = 5.00
areaItem.area = area
areaItem.photograph = photograph
areaItem.save()

figure = hmod.HistoricalFigure()
figure.name = 'Dr. Albrect'
figure.birthDate = '2015-03-07'
figure.birthPlace = 'tanner building'
figure.deathDate = '2015-03-07'
figure.deathPlace = 'the tanner'
figure.biographicalNote = 'a note about figure'
figure.isFictional = 'True'
figure.save()


role = hmod.Role()
role.user = user
role.area = area
role.name = 'role name...'
role.type = 'role type...'
role.historicalFigure = figure
role.save()


cat = hmod.Category()
cat.description = 'category 1'
cat.save()

photograph = hmod.Photograph()
photograph.imagePath = 'shoes.jpg'
photograph.save()

itemSpec = hmod.ItemSpecifications()
itemSpec.name = 'Black Shoes'
itemSpec.description = 'Normal Black Shoes'
itemSpec.price = '10.35'
itemSpec.manufacturer = 'shoes inc'
itemSpec.user = user
itemSpec.photograph = photograph
itemSpec.category = cat
itemSpec.save()

item = hmod.Item()
item.forSale = 'True'
item.quantityOnHand = '4'
item.cost = '4.44'
item.itemSpecifications = itemSpec
item.save()

photograph = hmod.Photograph()
photograph.imagePath = 'shoes2.jpg'
photograph.save()

itemSpec = hmod.ItemSpecifications()
itemSpec.name = 'Black Shoes /W Buckle'
itemSpec.description = 'Shoes with a fancy buckle'
itemSpec.price = '20.35'
itemSpec.manufacturer = 'fancy shoe inc'
itemSpec.user = user
itemSpec.photograph = photograph
itemSpec.category = cat
itemSpec.save()

item = hmod.Item()
item.forSale = 'True'
item.quantityOnHand = '2'
item.cost = '20.44'
item.itemSpecifications = itemSpec
item.save()


photograph = hmod.Photograph()
photograph.imagePath = 'petticoat.jpg'
photograph.save()

itemSpec = hmod.ItemSpecifications()
itemSpec.name = 'Womens White PettiCoat'
itemSpec.description = 'A sweet loking white petticoat with ornate inlaid flower design.'
itemSpec.price = '15.35'
itemSpec.manufacturer = 'old people'
itemSpec.user = user
itemSpec.photograph = photograph
itemSpec.category = cat
itemSpec.save()

item = hmod.Item()
item.forSale = 'True'
item.quantityOnHand = '4'
item.cost = '4.44'
item.itemSpecifications = itemSpec
item.save()


photograph = hmod.Photograph()
photograph.imagePath = 'stirrup_irons.jpg'
photograph.save()

itemSpec = hmod.ItemSpecifications()
itemSpec.name = 'Stirrup Irons'
itemSpec.description = 'Sturdy new handmade stirrup irons for horesback riding'
itemSpec.price = '20.00'
itemSpec.manufacturer = 'The Blacksmith'
itemSpec.user = user
itemSpec.photograph = photograph
itemSpec.category = cat
itemSpec.save()

item = hmod.Item()
item.forSale = 'True'
item.quantityOnHand = '4'
item.cost = '4.44'
item.itemSpecifications = itemSpec
item.save()


photograph = hmod.Photograph()
photograph.imagePath = 'teapot.jpg'
photograph.save()

itemSpec = hmod.ItemSpecifications()
itemSpec.name = 'Fancy Silver Teapot'
itemSpec.description = 'A silver teapot with floral design, and a wooden handel'
itemSpec.price = '350.00'
itemSpec.manufacturer = 'The Queen'
itemSpec.user = user
itemSpec.photograph = photograph
itemSpec.category = cat
itemSpec.save()

item = hmod.Item()
item.forSale = 'True'
item.quantityOnHand = '1'
item.cost = '200'
item.itemSpecifications = itemSpec
item.save()


photograph = hmod.Photograph()
photograph.imagePath = 'fakebell.jpg'
photograph.save()

itemSpec = hmod.ItemSpecifications()
itemSpec.name = 'Replica Liberty Bell'
itemSpec.description = 'Small brass replica of the liberty bell on a wooden base.'
itemSpec.price = '20.00'
itemSpec.manufacturer = 'John F. Street'
itemSpec.user = user
itemSpec.photograph = photograph
itemSpec.category = cat
itemSpec.save()

item = hmod.Item()
item.forSale = 'True'
item.quantityOnHand = '40'
item.cost = '10'
item.itemSpecifications = itemSpec
item.save()

photograph = hmod.Photograph()
photograph.imagePath = 'goves_breeches.jpg'
photograph.save()

itemSpec = hmod.ItemSpecifications()
itemSpec.name = 'Goves Breeches'
itemSpec.description = 'Red Breeches, with a 36 in waist'
itemSpec.price = '30.33'
itemSpec.manufacturer = 'Gove Allen'
itemSpec.user = user
itemSpec.photograph = photograph
itemSpec.category = cat
itemSpec.save()


rentalItem = hmod.RentalItem()
rentalItem.forSale = 'False'
rentalItem.quantityOnHand = '1'
rentalItem.cost = '20.22'
rentalItem.itemSpecifications = itemSpec
rentalItem.serialNumber = '123abc'
rentalItem.dateIn = '2015-03-07 12:01'
rentalItem.conditionNew = 'True'
rentalItem.notes = 'Goves Breeches Notes'
rentalItem.size = '36'
rentalItem.sizeModifier = '6'
rentalItem.gender = 'Male'
rentalItem.color = 'Red'
rentalItem.pattern = 'solid'
rentalItem.startYear = '1700-01-01'
rentalItem.endYear = '1750-01-01'
rentalItem.note = 'rental note for goves breeches'
rentalItem.timesRented = '3'
rentalItem.dailyPrice = '3.50'
rentalItem.save()


photograph = hmod.Photograph()
photograph.imagePath = 'meservys_breeches.jpg'
photograph.save()

itemSpec = hmod.ItemSpecifications()
itemSpec.name = 'Meservy''s Breeches'
itemSpec.description = 'Maron Breeches, with a 40 in waist'
itemSpec.price = '30.33'
itemSpec.manufacturer = 'Meservy'
itemSpec.user = user
itemSpec.photograph = photograph
itemSpec.category = cat
itemSpec.save()

rentalItem = hmod.RentalItem()
rentalItem.forSale = 'False'
rentalItem.quantityOnHand = '1'
rentalItem.cost = '6.55'
rentalItem.itemSpecifications = itemSpec
rentalItem.serialNumber = '123456'
rentalItem.dateIn = '2015-03-07 12:01'
rentalItem.conditionNew = 'False'
rentalItem.notes = 'Meservys Breeches Notes'
rentalItem.size = '40'
rentalItem.sizeModifier = '8'
rentalItem.gender = 'Male'
rentalItem.color = 'maroon'
rentalItem.pattern = 'solid'
rentalItem.startYear = '1710-01-01'
rentalItem.endYear = '1730-01-01'
rentalItem.note = 'rental note for meservys breeches'
rentalItem.timesRented = '3'
rentalItem.dailyPrice = '2.50'
rentalItem.save()


photograph = hmod.Photograph()
photograph.imagePath = 'overcoat.jpg'
photograph.save()

itemSpec = hmod.ItemSpecifications()
itemSpec.name = 'Red and Mustard Coat'
itemSpec.description = 'Long coat W/ brass buttons'
itemSpec.price = '300.33'
itemSpec.manufacturer = 'Chris int'
itemSpec.user = user
itemSpec.photograph = photograph
itemSpec.category = cat
itemSpec.save()

rentalItem = hmod.RentalItem()
rentalItem.forSale = 'False'
rentalItem.quantityOnHand = '1'
rentalItem.cost = '300.55'
rentalItem.itemSpecifications = itemSpec
rentalItem.serialNumber = '30154'
rentalItem.dateIn = '2015-03-07 12:01'
rentalItem.conditionNew = 'Trues'
rentalItem.notes = 'The coat is in great condition, note.'
rentalItem.size = '46'
rentalItem.sizeModifier = '42'
rentalItem.gender = 'Male'
rentalItem.color = 'Red'
rentalItem.pattern = 'solid'
rentalItem.startYear = '1700-01-01'
rentalItem.endYear = '1760-01-01'
rentalItem.note = 'rental note for coat'
rentalItem.timesRented = '0'
rentalItem.dailyPrice = '7.50'
rentalItem.save()


trans = hmod.Transaction()
trans.orderDate = '2015-03-07 12:01'
trans.phone = '8014224545'
trans.datePacked = '2015-03-07 12:01'
trans.datePaid = '2015-03-07 12:01'
trans.dateShipped = '2015-03-07 12:01'
trans.trackingNumber = '1234'
trans.placedBy = user
trans.handledBy = user
trans.shippingAddress = address
trans.save()


# lineItem = hmod.LineItem()
# lineItem.transaction = trans
# lineItem.save()


saleItem = hmod.SaleItem()
saleItem.transaction = trans
saleItem.quantity = '2'
saleItem.item = item
saleItem.save()

rental = hmod.Rental()
rental.transaction = trans
rental.rentalTime = '2015-03-01 12:01'
rental.dueDate = '2015-01-06 12:01'
# rental.returnTime = models.DateTimeField(null=True, blank=True, auto_now=False, auto_now_add=False)
rental.discountPercent = .10
rental.rentalItem = rentalItem
rental.save()

rental = hmod.Rental()
rental.transaction = trans
rental.rentalTime = '2015-03-01 12:01'
rental.dueDate = '2015-02-06 12:01'
# rental.returnTime = models.DateTimeField(null=True, blank=True, auto_now=False, auto_now_add=False)
rental.discountPercent = .10
rental.rentalItem = rentalItem
rental.save()

rental = hmod.Rental()
rental.transaction = trans
rental.rentalTime = '2015-03-01 12:01'
rental.dueDate = '2015-03-06 12:01'
# rental.returnTime = models.DateTimeField(null=True, blank=True, auto_now=False, auto_now_add=False)
rental.discountPercent = .10
rental.rentalItem = rentalItem
rental.save()

rental = hmod.Rental()
rental.transaction = trans
rental.rentalTime = '2015-03-01 12:01'
rental.dueDate = '2015-04-06 12:01'
# rental.returnTime = models.DateTimeField(null=True, blank=True, auto_now=False, auto_now_add=False)
rental.discountPercent = .10
rental.rentalItem = rentalItem
rental.save()

rental = hmod.Rental()
rental.transaction = trans
rental.rentalTime = '2015-03-01 12:01'
rental.dueDate = '2015-03-06 12:01'
rental.returnTime = '2015-03-05 12:01'
rental.discountPercent = .10
rental.rentalItem = rentalItem
rental.save()


rental = hmod.Rental()
rental.transaction = trans
rental.rentalTime = '2015-03-01 12:01'
rental.dueDate = '2015-03-06 12:01'
rental.returnTime = '2015-03-07 12:01'
rental.discountPercent = .10
rental.rentalItem = rentalItem
rental.save()


# return1 = hmod.Return()
# return1.transaction = trans
# return1.feeWaived = 'False'
# return1.forRental = rental
# return1.save()


lateFee = hmod.LateFee()
lateFee.transaction = trans
lateFee.feeWaived = 'False'
lateFee.forRental = rental
lateFee.daysLate = '1'
lateFee.save()


damageFee = hmod.DamageFee()
damageFee.transaction = trans
damageFee.feeWaived = 'False'
damageFee.forRental = rental
damageFee.description = 'description of damage...'
damageFee.damagePrice = '10.25'
damageFee.save()

print('Models Filled')
