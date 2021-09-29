from django.contrib import admin
from .models import Contact


# Register your models here.

class ContactAdmin(admin.ModelAdmin):

    readonly_fields = ('name', 'email', 'message',)

    list_display = (
        'name',
        'email',
    )

    ordering = ('-pk',)


admin.site.register(Contact, ContactAdmin)
