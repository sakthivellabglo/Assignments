from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        #parser.add_argument('total', type=int, help='Indicates the number of users to be created')

        # Optional argument
        parser.add_argument('-p', '--prefix', type=str, help='Define a username prefix', )
        parser.add_argument('-b', '--pre', type=str, help='Define a username prefix', ) 

    def handle(self, *args, **kwargs):
        prefix = kwargs['prefix']
        password =  kwargs['pre']
        if prefix:
                username = '{prefix}'.format(prefix=prefix)
        else:
                username = get_random_string(7)
        User.objects.create_user(username=username, email='', password=password)
        print("created")         