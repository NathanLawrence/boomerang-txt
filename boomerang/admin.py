from django.contrib import admin

from .models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')

class SimpleAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'message', 'delivery_date')
    list_filter = ['recipient']

admin.site.register(User, UserAdmin)
admin.site.register(SimpleMSG, SimpleAdmin)
admin.site.register(RepeatMSG)