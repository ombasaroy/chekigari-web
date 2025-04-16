from django.db import models
import uuid


# Create your models here.

class Make(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    

class Body_type(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Body_type'
        verbose_name_plural = 'Body Types'


class Vehicle_registration_detail(models.Model):

    FUEL_TYPE_CHOICES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
    ]

    TRANSMISSION_CHOICES = [
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual'),
    ]
    
    registration_number = models.CharField(max_length=100, unique=True)
    make = models.ForeignKey(Make, on_delete=models.SET_NULL, null=True)
    body_type = models.ForeignKey(Body_type, on_delete=models.SET_NULL, null=True)
    manufacturer_year = models.IntegerField()
    engine_capacity = models.IntegerField()
    color = models.CharField(max_length=100)
    fuel_type = models.CharField(choices=FUEL_TYPE_CHOICES, max_length=100)
    transmission = models.CharField(choices=TRANSMISSION_CHOICES, max_length=100)
    passanger_capacity = models.IntegerField()
    number_of_doors = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.registration_number
    
    class Meta:
        verbose_name = 'Vehicle_registration_detail'
        verbose_name_plural = 'Vehicle Registration Details'



class CollisionType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class DamageSeverity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = 'Damage_severity'
        verbose_name_plural = 'Damage Severities'


class AccidentReport(models.Model):
    report_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vehicle_registration_number = models.ForeignKey(Vehicle_registration_detail, on_delete=models.CASCADE)
    accident_date = models.DateTimeField(auto_now_add=True)
    collision_type = models.ForeignKey(CollisionType, on_delete=models.SET_NULL, null=True)
    damage_severity = models.ForeignKey(DamageSeverity, on_delete=models.SET_NULL, null=True)
    accident_location = models.CharField(max_length=100)
    accident_description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vehicle_registration_number.registration_number


