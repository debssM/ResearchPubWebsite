from django.core.management.base import BaseCommand
from PaperCore.models import Title

class Command(BaseCommand):

    help = 'Init a default title'

    def handle(self, *args, **options):
        Title.objects.create(
            page_title='Paper Gallery'
        )

