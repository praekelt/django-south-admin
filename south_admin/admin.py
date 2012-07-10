from django.contrib import admin
from south.models import MigrationHistory


class MigrationHistoryAdmin(admin.ModelAdmin):
    list_display = ('app_name', 'migration', 'applied')

admin.site.register(MigrationHistory, MigrationHistoryAdmin)
