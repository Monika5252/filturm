from django.contrib import admin

# Register your models here.
# from abhi.models import *

from .models import *


@admin.register(filturm)
class filturmadmin(admin.ModelAdmin):
    list_display = ['filturmid','fname']

admin.site.register(Login)
admin.site.register(em)
admin.site.register(EmpLeave)
admin.site.register(TimeEntry)

# admin.site.register(filturm)
# @admin.register.site(filturm)
