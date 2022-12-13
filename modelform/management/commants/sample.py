from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    help = 'Displays current time'


    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        print("It's now %s" % time)