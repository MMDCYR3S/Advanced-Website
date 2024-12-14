from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User, Profile
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Create a Custom Creation form
# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ("email",)

# Create a custom user admin model for admin panel
class CustomUserAdmin(UserAdmin):
    model = User
    # add_form = CustomUserCreationForm
    list_display = ("email", "is_active", "is_staff", "is_superuser")
    list_filter = ("email", "is_active")
    searching_field = ("email",)
    ordering = ("email", )
    fieldsets = (
        ("Authentication",{
            "fields":('email', 'password'),
        }),

        ("Permissions",{
            "fields":('is_active', 'is_staff', 'is_superuser'),
        }),

        ("Groups Permissions",{
            "fields":('groups', 'user_permissions'),
        }),

        ("Important Dates",{
            "fields":('last_login',),
        }),
    )
    add_fieldsets = (
        ("Authentication",{
            'classes' : ("wide",),
            "fields" : ('email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
