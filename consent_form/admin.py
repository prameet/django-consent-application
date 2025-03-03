# from django.contrib import admin
# from django.utils.html import format_html
# from .models import ConsentForm


# @admin.register(ConsentForm)
# class ConsentFormAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'service_code', 'application', 'uploaded_at')
#     search_fields = ('service_code', 'user__email', 'participant_full_name', 'ndis_number')
#     list_filter = ('application', 'uploaded_at', 'declaration')
#     ordering = ('-uploaded_at',)
#     readonly_fields = ('uploaded_at', 'consent_pdf')

#     # def consent_pdf_link(self, obj):
#     #     """Display a link to the consent PDF in the admin panel."""
#     #     if obj.consent_pdf:
#     #         return format_html('<a href="{}" target="_blank">View PDF</a>', obj.consent_pdf.url)
#     #     return "No PDF"

#     # consent_pdf_link.short_description = "Consent PDF"


from django.contrib import admin
from django import forms
from .models import ConsentForm

class ConsentFormAdminForm(forms.ModelForm):
    
    class Meta:
        model = ConsentForm
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        
        # Suppress validation messages only in admin
        if 'admin' in self.request.path:
            self._errors.clear()  # This removes all validation errors

        return cleaned_data

class ConsentFormAdmin(admin.ModelAdmin):
    form = ConsentFormAdminForm
    list_display = ('id', 'user', 'service_code', 'application', 'uploaded_at')
    search_fields = ('service_code', 'user__email', 'participant_full_name', 'ndis_number')
    list_filter = ('application', 'uploaded_at', 'declaration')
    ordering = ('-uploaded_at',)
    readonly_fields = ('uploaded_at', 'consent_pdf')
    
    

admin.site.register(ConsentForm, ConsentFormAdmin)
