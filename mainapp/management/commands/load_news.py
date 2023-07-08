from django.core.management.base import BaseCommand
from django.conf import settings

from balaboba import Balaboba
from datetime import datetime
import json
import os
            
bb = Balaboba()
news = []


class Command(BaseCommand):
    help = 'usage load_news {news_count}'

    def handle(self, *args, **options):
        if not options['news_count']:
            return
        _load_news(options['news_count'])
        with open(os.path.join(settings.BASE_DIR, 'data/news.json'), 'w') as f:
            json.dump(news, f)

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '--news_count',
            type=int,
            dest='news_count',
        )


def get_news():
    n = {}
    n["title"] = f"Новость {len(news) + 1}"
    n["date"] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    text_types = bb.get_text_types(language="ru")
    n['description'] = bb.balaboba("Новости", text_type=text_types[1])
    return n

def _load_news(news_count: int):
    for i in range(1, news_count + 1):
        print(f"Новость {i} из {news_count}")
        news.append(get_news())
