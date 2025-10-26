from typing import Any, Callable, Dict, List, Optional, Tuple, Union


def extract_nested_value(obj: Any, keys: List[str], none: Any = None) -> Any:
    """
    функция измлекает значение из вложенного словаря/списка по цепочке ключей,
    если путь не существует — возвращает none.
    """
    current = obj
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        elif isinstance(current, list) and key.isdigit():
            idx = int(key)
            if 0 <= idx < len(current):
                current = current[idx]
            else:
                return none
        else:
            return none
    return current
