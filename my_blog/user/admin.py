from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user.models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
  pass
  # fieldsets = (
  #   (None, {'fields': ('username', 'password')}),
  #   ('Informacon personal', {'fields': ('first_name', 'last_name', 'email')})
  #   ('redes sociales', {'fields': ('web_site',)})
  # )



