import requests
from laureates_configs import process_persons, process_orgs 

# URL API Нобелевской премии
URL_LAUREATES = "https://api.nobelprize.org/v2/laureates?limit=1200"


def get_laureate_data(laureate: dict) -> dict:
    """
    Определяет тип лауреата и соотв образом обрабатывает данные.
    
    Args:
        laureate: Dictionary with laureate data

    Returns:
        Processed laureate data with added 'type_' field ('person' or 'org')
    """
    if "knownName" in laureate:
        processed = process_persons(laureate)
        processed["type_"] = "person"
    elif "orgName" in laureate:
        processed = process_orgs(laureate)
        processed["type_"] = "organization"
    else:
        # неизвестный тип, вдруг попадется
        return {"id": laureate.get("id", "unknown"), "type_": "unknown"}

    return processed


def main():
    print("Выгрузка данных из АПИ о лауреатах...")
    laureates_response = requests.get(URL_LAUREATES)
    laureates_response.raise_for_status()
    laureates = laureates_response.json()

    print(f"Выгружено из АПИ {len(laureates['laureates'])} записей о лауретах")

    laureates_data = []
    for laureate in laureates['laureates']:
        processed = get_laureate_data(laureate)
        laureates_data.append(processed)

    print(f"Обработано {len(laureates_data)} записей о лауреатах")

    #выведу первых 2-х
    for i, item in enumerate(laureates_data[:2]):
        print(f"\nЛауреат {i+1}")
        print(item)


if __name__ == "__main__":
    main()