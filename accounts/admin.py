from django.contrib import admin
from .models import UserAccountPortfolio


class UserAccountAdmin(admin.ModelAdmin):
    """
    Displaying Users account balance in admin dashboard.
    Easier for implementing or adding balance to users if it
    it lost.
    """
    list_display = ('user', 'balance')

admin.site.register(UserAccountPortfolio, UserAccountAdmin)
