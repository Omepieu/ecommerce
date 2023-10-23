from django.contrib import admin
from count.models import Client

# Register your models here.
admin.sites.AdminSite.site_header = "Superette Shopping" 
admin.sites.AdminSite.index_title = "Manageur de Superette Shopping"
admin.sites.AdminSite.site_title = "Shopping"

class ClientAdmin(admin.ModelAdmin):
    list_display = ('user','telephone','date_naiss', 'sexe')

admin.site.register(Client, ClientAdmin)