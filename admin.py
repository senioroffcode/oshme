from django.contrib import admin
from .models import *

admin.site.register(Country)
admin.site.register(Category)
admin.site.register(Region)
admin.site.register(Town)
admin.site.register(Place)