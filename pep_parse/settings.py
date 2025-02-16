from pathlib import Path

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = 'results'

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
    },
}

PEP_NAME = 'pep'
PEP_ALLOWED_DOMAINS = ['peps.python.org']
PEP_START_URLS = [f'https://{domain}/' for domain in PEP_ALLOWED_DOMAINS]
