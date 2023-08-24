from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Description of your command'

    def handle(self, *args, **kwargs):
        # Your command logic here
        return 