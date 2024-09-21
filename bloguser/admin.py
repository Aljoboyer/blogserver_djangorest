from django.contrib import admin
from . models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'password', 'about', 'profileImg']
      # This ensures the UUID field is used properly in the admin
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['id'].disabled = True  # Disable the UUID field in the admin form
        return form
    