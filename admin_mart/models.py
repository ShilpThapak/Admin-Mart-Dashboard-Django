from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

LOCATION_CHOICES = (
    ('CH', 'Corporate Headpffice'),
    ('OD', 'Operations Department'),
    ('WS', 'Work Station'),
    ('MD', 'Marketing Division'),
)

INITIAL_SEVERITY_CHOICES = (
    ('Mild', 'Mild'),
    ('Moderate', 'Moderate'),
    ('Severe', 'Severe'),
    ('Fatal', 'Fatal')
)

SUB_INCIDENT_CHOICES = (
    ('Environmental Incident', 'Environmental Incident'),
    ('Injury/Illness', 'Injury/Illness'),
    ('Property Damage', 'Property Damage'),
    ('Vehicle', 'Vehicle')
)

class Incident(models.Model):
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES)
    department = models.TextField()
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    incident_location = models.TextField()
    initial_severity = models.CharField(max_length=10, choices=INITIAL_SEVERITY_CHOICES)
    suspected_cause = models.TextField()
    immediate_action_taken = models.TextField()
    sub_incident_types = models.CharField(max_length=100, choices=SUB_INCIDENT_CHOICES)
    reported_by = models.ForeignKey(User, on_delete=CASCADE)
    saved = models.BooleanField()

    