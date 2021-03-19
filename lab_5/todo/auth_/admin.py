from django.contrib import admin
from .models import MainUser


@admin.register(MainUser)
class MainUser(admin.ModelAdmin):
    list_display = ('username', 'email', 'last_login',
                    'date_joined', 'location')
    search_fields = ('username', 'location')
    ordering = ('last_login', )
    list_filter = ('location', )

    def reset_location(self, request, queryset, *args, **kwargs):
        queryset.update(location='KZ')
    reset_location.short_description = 'Reset Location to default: KZ'
    actions = [reset_location]
