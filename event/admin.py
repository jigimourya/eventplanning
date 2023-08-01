from django.contrib import admin

# Register your models here.

from .models import CustomUser, Organiser, Category, Department




@admin.register(Organiser)
class EventInstanceAdmin(admin.ModelAdmin):
    """Administration object for Organiser models.
    Defines:
     - fields to be displayed in list view (list_display)
     - filters that will be displayed in sidebar (list_filter)
     - grouping of fields into sections (fieldsets)
    """
    list_display = ('name_of_event', 'event_type', 'id')
    list_filter = ('event_type',)

    fieldsets = (
        (None, {
            'fields': ( 'user_id', 'event_type', 'name_of_event', 'description', 'department', 'for_batch', 'event_date', 'venue', 'time', 'mode', 'organiser_name', 'organiser_phone', 'organiser_email', 'last_date_to_register', 'avatar' )
        }),
    )

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """Administration object for Author models.
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields),
       grouping the date fields horizontally
     
    """
    list_display = (
                    'first_name', 'phone', 'email')
    fields = ['first_name', 'phone', 'email']
    inlines = []


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Administration object for Organiser models.
    Defines:
     - fields to be displayed in list view (list_display)
     - filters that will be displayed in sidebar (list_filter)
     - grouping of fields into sections (fieldsets)
    """
    list_display = ('category_name', 'creation_date', 'id')
    list_filter = ('category_name',)

    fieldsets = (
        (None, {
            'fields': ( 'category_name', 'creation_date' )
        }),
    )


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    """Administration object for Organiser models.
    Defines:
     - fields to be displayed in list view (list_display)
     - filters that will be displayed in sidebar (list_filter)
     - grouping of fields into sections (fieldsets)
    """
    list_display = ('department_name', 'creation_date', 'id')
    list_filter = ('department_name',)

    fieldsets = (
        (None, {
            'fields': ( 'department_name', 'creation_date' )
        }),
    )