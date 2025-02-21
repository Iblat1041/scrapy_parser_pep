import csv
import datetime as dt
from collections import defaultdict

from scrapy.exceptions import DropItem

from pep_parse.settings import (
    BASE_DIR, DATETIME_FORMAT, RESULTS_DIR, TABLE_HEADERS, TABLE_TOTAL
    )


class PepParsePipeline:
    """
    Pipeline для подсчета статусов PEP и сохранения результатов в CSV-файл.
    """

    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        """
        Инициализирует словарь для подсчета статусов PEP при открытии паука.
        """
        self.pep_status_counts = defaultdict(int)

    def process_item(self, item, spider):
        """Обрабатывает каждый PEP и подсчитывает его статус."""
        pep_status = item.get('status')
        if pep_status is None:
            raise DropItem(f'Неизвестный статус pep - {item}')
        self.pep_status_counts[pep_status] += 1
        return item

    def close_spider(self, spider):
        """
        Сохраняет результаты подсчета статусов PEP в CSV-файл
        при закрытии паука.
        """
        now_format_time = dt.datetime.now().strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_format_time}.csv'
        file_path = self.results_dir / file_name
        with open(file_path, 'w', encoding='utf-8') as f:
            csv.writer(
                f,
                dialect='unix',
            ).writerows(
                TABLE_HEADERS,
                *self.pep_status_counts.items(),
                (TABLE_TOTAL, sum(self.pep_status_counts.values()))
            )
