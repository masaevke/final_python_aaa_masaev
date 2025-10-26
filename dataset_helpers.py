from typing import List, Dict, Any, Callable, Tuple, Union, Optional
from collections import defaultdict


def filter_data(data: List[Dict], conditions: Dict[str, Any]) -> List[Dict]:
    """
    функция фильтрует список словарей по условиям

    Args:
        data: список словарей для фильтрации
        conditions: словарь {поле: значение} или {поле: функция-условие}

    Returns:
        отфильтрованный список
    """
    filtered = []
    for item in data:
        match = True
        for field, condition in conditions.items():
            if callable(condition):
                if not condition(item.get(field)):
                    match = False
                    break
            else:
                if item.get(field) != condition:
                    match = False
                    break
        if match:
            filtered.append(item)
    return filtered


def group_by_attributes(
    data: List[Dict], attributes: List[str]
) -> Dict[Tuple, List[Dict]]:
    """
    функция группирует данные по указанным атрибутам

    Args:
        data: список словарей для группировки
        attributes: список полей для группировки

    Returns:
        словарь {кортеж_значений: список_элементов}
    """
    grouped = defaultdict(list)
    for item in data:
        key = tuple(item.get(attr) for attr in attributes)
        grouped[key].append(item)
    return dict(grouped)


def apply_aggregation(
    data: List[Dict], aggregation_func: Callable, field: Optional[str] = None
) -> Any:
    """
    Применяет агрегационную функцию к данным

    Args:
        data: список словарей
        aggregation_func: функция агрегации
        field: поле для агрегации (если None, передаются все данные)

    Returns:
        результат агрегации
    """
    if field:
        values = [item.get(field) for item in data if item.get(field) is not None]
        return aggregation_func(values) if values else None
    else:
        return aggregation_func(data)
