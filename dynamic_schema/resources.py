from import_export import resources
from .models import YourModel  # Replace with your model name

class YourModelResource(resources.ModelResource):
    class Meta:
        model = YourModel
