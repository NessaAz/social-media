from django.contrib import admin
from django.contrib.auth.models import Group

#unregister Groups 
admin.site.unregister(Group)

