from django.contrib import admin
from products.models import Contact_us

admin.site.site_header = "Tasty Bytes | Admin"

class ContactAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "subject", "added_on", "is_approved"]

admin.site.register(Contact_us, ContactAdmin)