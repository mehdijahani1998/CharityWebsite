from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from accounts.models import User


@admin.register(User)
class UserAdmin(DefaultUserAdmin):

    def custom_titled_filter(title):
        class Wrapper(admin.FieldListFilter):
            def __new__(cls, *args, **kwargs):
                instance = admin.FieldListFilter.create(*args, **kwargs)
                instance.title = title
                return instance
        return Wrapper

    # @admin.display(description='STAFF STATUS')
    # def staff_status(self):
    #     return self.is_staff

    @admin.display(description='EMAIL ADDRESS')
    def email_address(self):
        return self.email
    
    # @admin.display(description='ACTIVE')
    # def active_status(self):
    #     return self.is_active

    def is_active(self, obj):
        return obj.is_active
    is_active.verbose_name = 'ACTIVE'
    is_active.boolean = True
    is_active.editable = True

    list_display = ('username', email_address, 'first_name', 'last_name', 'is_staff', 'is_active')
    list_editable = (
        'is_active',
        'is_staff',
    )
    sortable_by = ['username']
    list_filter = (
        'gender',
        ('is_staff', custom_titled_filter("staff status")),
        ('is_superuser', custom_titled_filter("superuser status")),
        ('is_active', custom_titled_filter("active")),
    )
