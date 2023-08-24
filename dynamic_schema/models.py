from django.db import models

class CustomSchema(models.Model):
    name = models.CharField(max_length=255)
    field_name = models.CharField(max_length=255)
    field_type_choices = [
    ('CharField', 'CharField'),
    ('IntegerField', 'IntegerField'),
    # Add other field types as needed
]

    field_type = models.CharField(max_length=50, choices=field_type_choices)
    max_length = models.PositiveIntegerField(null=True, blank=True)
    # Add other attributes as necessary

