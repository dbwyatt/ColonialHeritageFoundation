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


event = hmod.Event()
event.name = 'The Event!'
event.description = 'nothing is happening at the event, sorry'
event.startDate = '2015-03-07 12:01'
event.endDate = '2015-03-07 12:02'
event.mapFileName = 'a map here?'
event.venueName = 'Tanner Building'
event.address = address
event.save()


area = hmod.Area()
area.name = 'IS core'
area.description = 'where good men suffer'
area.placeNumber = '1'
area.coordinatingAgent = user
area.supervisingAgent = user
area.event = event
area.save()


areaItem = hmod.AreaSaleItem()
areaItem.name = 'area sale item...'
areaItem.description = 'description of an area sale item'
areaItem.lowPrice = 1.00
areaItem.highPrice = 1.01
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


itemSpec = hmod.ItemSpecifications()
itemSpec.name = 'item spec name...'
itemSpec.description = 'item spec description...'
itemSpec.price = '10.35'
itemSpec.manufacturer = 'item spec manufacturer'
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


# serialItem = hmod.SerializedItem()
# serialItem.serialNumber = 'abc123'
# serialItem.dateIn = '2015-03-07 12:01'
# serialItem.conditionNew = 'True'
# serialItem.notes = 'serial item notes...'
# serialItem.save()
#
#
# wardItem = hmod.WardrobeItem()
# wardItem.size = '5'
# wardItem.sizeModifier = '6'
# wardItem.gender = 'Male'
# wardItem.color = 'blue'
# wardItem.pattern = 'pattern is lame'
# wardItem.startYear = '2000-01-01'
# wardItem.endYear = '2010-01-01'
# wardItem.note = 'wardrobe item note...'
# wardItem.save()


rentalItem = hmod.RentalItem()
rentalItem.forSale = 'True'
rentalItem.quantityOnHand = '5'
rentalItem.cost = '5.55'
rentalItem.itemSpecifications = itemSpec
rentalItem.serialNumber = 'abc123'
rentalItem.dateIn = '2015-03-07 12:01'
rentalItem.conditionNew = 'True'
rentalItem.notes = 'serial item notes...'
rentalItem.size = '5'
rentalItem.sizeModifier = '6'
rentalItem.gender = 'Male'
rentalItem.color = 'blue'
rentalItem.pattern = 'pattern is lame'
rentalItem.startYear = '2000-01-01'
rentalItem.endYear = '2010-01-01'
rentalItem.note = 'wardrobe item note...'
rentalItem.timesRented = '1'
rentalItem.dailyPrice = '2.50'
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
rental.dueDate = '2015-03-06 12:01'
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
