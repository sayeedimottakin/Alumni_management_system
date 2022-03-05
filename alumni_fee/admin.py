from django.contrib import admin

# Register your models here.
from .models import Fee_Info,Alumni_Fee,Alumni_Yearly_Fee
admin.site.register(Fee_Info)
admin.site.register(Alumni_Fee)
admin.site.register(Alumni_Yearly_Fee)
# class AlumniYearlyFeeAdmin(admin.ModelAdmin):
#     list_display = ("amount", "year")
