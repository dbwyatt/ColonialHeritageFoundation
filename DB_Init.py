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

# #### CREATE PERMISSIONS/GROUPS #####################
# Permission.objects.all().delete()
# Group.objects.all().delete()

# permissionU = Permission()
# permissionU.codename = 'User'
# permissionU.content_type = ContentType.objects.get(id=9)
# permissionU.name = 'Has User Rights'
# permissionU.save()
User = Group()
User.name = "User"
User.save()
# User.permissions.add(permissionU)
#
# permissionM = Permission()
# permissionM.codename = 'Manager'
# permissionM.content_type = ContentType.objects.get(id=8)
# permissionM.name = 'Has Manager Rights'
# permissionM.save()
Manager = Group()
Manager.name = "Manager"
Manager.save()
# Manager.permissions.add(permissionM, permissionU)
#
# permissionA = Permission()
# permissionA.codename = 'Admin'
# permissionA.content_type = ContentType.objects.get(id=7)
# permissionA.name = 'Has Admin Rights'
# permissionA.save()
Admin = Group()
Admin.name = "Admin"
Admin.save()
# Admin.permissions.add(permissionA, permissionM, permissionU)


permissions = Permission.objects.all()
for x in permissions:
    Admin.permissions.add(x)

print('permissions initialized')


# ########### MAKE USERS ####################

# create null address and let the users point to it
photograph = hmod.Photograph()
photograph.imagePath = 'photograph'
photograph.save()

address = hmod.Address()
address.address1 = 'address'
address.address2 = 'address'
address.city = 'address'
address.state = 'address'
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
user.is_superuser = False
user.address = address
user.photograph = photograph
user.save()
user.groups.add(Admin)

user = hmod.User()
user.username = 'NickSucks'
user.last_name = "Nick"
user.first_name = "Stevens"
user.email = 'NS@gmail.com'
user.security_question = "School?"
user.security_answers = "BYU"
user.set_password('ilikeadodadjango')
user.is_superuser = False
user.address = address
user.photograph = photograph
user.save()
user.groups.add(User)