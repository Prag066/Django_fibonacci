from django.contrib import admin

from .models import Fib_data

class FibAdmin(admin.ModelAdmin):
    list_display = ['number','duretion']
admin.site.register(Fib_data,FibAdmin)
