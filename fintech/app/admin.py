from django.contrib import admin
from .models import Contact,ContactSubmission
 

admin.site.register(Contact)

class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email_address', 'phone_no', 'message')
    search_fields = ('full_name', 'email_address', 'phone_no')
admin.site.register(ContactSubmission)
# class ContactSubmissionAdmin(admin.ModelAdmin):
#     list_display = ('full_name', 'email_address', 'phone_no', 'message')
#     search_fields = ('full_name', 'email_address', 'phone_no')