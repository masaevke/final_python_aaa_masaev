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


CONFIG_PERSON = {
    "id": ["id"],
    "name": ["knownName", "en"],
    "gender": ["gender"],
    "birth_year": (["birth", "date"], process_year),
    "country_birth": ["birth", "place", "country", "en"],
    "country_now": ["birth", "place", "countryNow", "en"],
    #обрабатывается процессором призов, который вы задаете в конфиге для призов
    "prizes_relevant": (["nobelPrizes"], lambda prizes: prizes) 
}

CONFIG_ORG = {
    "id": ["id"],
    "name": ["orgName", "en"],
    "founded_year": (["founded", "date"], process_year),
    "country_founded": ["founded", "place", "country", "en"],
    "country_now": ["founded", "place", "countryNow", "en"],
    #обрабатывается процессором призов, который вы задаете в конфиге для призов
    "prizes_relevant": (["nobelPrizes"], lambda prizes: prizes)  
}


def person_processor():
    return create_processor(CONFIG_PERSON, list_processor=False)

def org_processor():
    return create_processor(CONFIG_ORG, list_processor=False)