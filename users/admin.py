from django.contrib import admin
from django.contrib.auth import  get_user_model
from django.contrib.auth.admin import UserAdmin


from users.models import User

@admin.register(User)
class UserAdmin(UserAdmin):
    pass
    # list_display = ('username', 'first_name', 'last_name', 'email', 'is_active',)
    # list_display = '_all_'

# admin.site.register(User)
