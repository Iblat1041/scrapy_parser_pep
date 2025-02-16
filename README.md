<h1 align='center'> Асинхронный парсер документации PEP </h1>

Репозиторий содержит проект для парсинга документации PEP  с использованием фреймворка Scrapy. Парсер собирает информацию о каждом PEP, включая номер, название и статус, и сохраняет ее в двух CSV-файлах: один содержит список всех PEP, а другой — сводку по статусам.

<h2 align='center'>  Структура проекта </h2>

```
scrapy_parser_pep
 ├── pep_parse/
     ├── spiders/
         ├── __init__.py
         └── pep.py
     ├── __init__.py
     ├── items.py
     ├── middlewares.py
     ├── pipelines.py
     └── settings.py
 ├── results/
 ├── tests/
   └── <содержимое tests>
 ├── .flake8
 ├── .gitignore
 ├── README.md
 ├── pytest.ini
 ├── requirements.txt
 └── scrapy.cfg
```

<h2 align='center'> Зависимости </h2>

Зависимости проекта указаны в файле `requirements.txt`. Для установки зависимостей:

```bash
pip install -r requirements.txt
```

<h2 align='center'>Запуск парсера </h2>

1. Создайте и активируйте виртуальное окружение.
2. Установите зависимости: `pip install -r requirements.txt`.
3. Запустите парсер следующей командой из корневой директории проекта:

```bash
scrapy crawl pep
```

<h2 align='center'> Результаты </h2>

Результаты парсинга сохраняются в директории `results/` в двух CSV-файлах:

- `pep_ДатаВремя.csv`: содержит список всех PEP с номерами, названиями и статусами.
- `status_summary_ДатаВремя.csv`: содержит сводку по статусам PEP, включая общее количество PEP (Total).

<h2 align='center'>Тестирование </h2>

Тесты для проекта находятся в директории `tests/`. Для их выполнения:

```bash
pytest
```


## Автор: [Брежнев Иван](https://github.com/Blathata)
