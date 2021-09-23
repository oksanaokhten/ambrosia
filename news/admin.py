from django.contrib import admin
from .models import News


# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'admin_name',
        'admin_profession',
        'image',
        'date',
    )
    ordering = ('-date',)


admin.site.register(News, NewsAdmin)
