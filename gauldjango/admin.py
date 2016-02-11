from django.contrib import admin

from gauldjango.models import  GAULAdmin0, GAULAdmin1, GAULAdmin2

class GAULAdmin0Admin(admin.ModelAdmin):
    model = GAULAdmin0
    list_display_links = ('admin0_name',)
    list_display = ('admin0_code','admin0_name', 'disp_area', 'status', )

class GAULAdmin1Admin(admin.ModelAdmin):
    model = GAULAdmin1
    list_display_links = ('admin1_name',)
    list_display = ('admin1_code','admin1_name', 'disp_area', 'status', )

class GAULAdmin2Admin(admin.ModelAdmin):
    model = GAULAdmin2
    list_display_links = ('admin2_name',)
    list_display = ('admin2_code','admin2_name', 'disp_area', 'status', )

admin.site.register(GAULAdmin0, GAULAdmin0Admin)
admin.site.register(GAULAdmin1, GAULAdmin1Admin)
admin.site.register(GAULAdmin2, GAULAdmin2Admin)
