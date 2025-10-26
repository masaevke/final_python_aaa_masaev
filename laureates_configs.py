from json_dict_processing import create_processor
from typing import Optional


def process_year(year_string: str) -> Optional[int]:
    """вспомогательная -
    извлекает год из строки в формате 'YYYY-MM-DD'."""
    if not year_string or not isinstance(year_string, str):
        return None
    try:
        return int(year_string[:4])
    except ValueError:
        return None
