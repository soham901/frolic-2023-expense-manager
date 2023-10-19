from django.contrib import admin
from .models import *


admin.site.site_header = "Expense Tracker Admin"

admin.site.register(Expence)
admin.site.register(Income)
