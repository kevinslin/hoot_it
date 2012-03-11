from main.models import *
from django.contrib import admin

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age')


admin.site.register(UserProfile, ProfileAdmin)
