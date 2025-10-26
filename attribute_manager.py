from typing import List, Dict, Callable


def add_field(data: List[Dict], field_name: str, field_func: Callable) -> List[Dict]:
    """
    фнукция добавляет новое поле к каждому элементу данных

    Args:
        data: список словарей
        field_name: имя нового поля
        field_func: функция, вычисляющая значение поля

    Returns:
        обновленные данные
    """
    for item in data:
        item[field_name] = field_func(item)
    return data


def remove_field(data: List[Dict], field_name: str) -> List[Dict]:
    """
    функция удаляет поле из каждого элемента данных
    """
    for item in data:
        item.pop(field_name, None)
    return data


def transform_field(
    data: List[Dict], field_name: str, transform_func: Callable
) -> List[Dict]:
    """
    функция изменяет существующее поле
    """
    for item in data:
        if field_name in item:
            item[field_name] = transform_func(item[field_name])
    return data
