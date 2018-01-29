from django.contrib import admin
from models import SilicaPacket, Color, Language, Manufacturer

class PacketAdmin(admin.ModelAdmin):
    list_display = ('description', 'text', 'manufacturer_id')
    search_fields = ('description', 'text')

admin.site.register(SilicaPacket, PacketAdmin)
admin.site.register(Color)
admin.site.register(Language)
admin.site.register(Manufacturer)
