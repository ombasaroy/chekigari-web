from django.contrib import admin
from .models import Vehicle_registration_detail, Make, Body_type, CollisionType, DamageSeverity, AccidentReport

# Register your models here.
class Vehicle_registration_detailAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'make', 'body_type', 'manufacturer_year', 'engine_capacity', 'color', 'fuel_type', 'transmission', 'passanger_capacity', 'number_of_doors')
admin.site.register(Vehicle_registration_detail, Vehicle_registration_detailAdmin)

admin.site.register(Make)
admin.site.register(Body_type)


class CollisionTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
admin.site.register(CollisionType, CollisionTypeAdmin)


class DamageSeverityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
admin.site.register(DamageSeverity, DamageSeverityAdmin)


class AccidentReportAdmin(admin.ModelAdmin):
    list_display = ('report_id', 'get_registration_number', 'collision_type', 'damage_severity', 'date_created', 'date_updated')

    def get_registration_number(self, obj):
        return obj.vehicle_registration_number.registration_number

    get_registration_number.short_description = 'Registration Number'  # optional, for admin column label
admin.site.register(AccidentReport, AccidentReportAdmin)

