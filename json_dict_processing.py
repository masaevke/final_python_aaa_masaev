from typing import Any, Callable, Dict, List, Tuple, Union


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


def process_dictionary_with_config(
    dictionary: Dict, config: Dict[str, Union[List[str], Tuple[List[str], Callable]]]
) -> Dict[str, Any]:
    """
    функция обрабатывает один словарь согласно {атрибут: path_list} или {атрибут: (path_list, transform_func)}
    """
    result = {}
    for attr_name, spec in config.items():
        if isinstance(spec, tuple):
            path_list, transform = spec
            raw_value = extract_nested_value(dictionary, path_list)
            if raw_value is not None:
                try:
                    result[attr_name] = transform(raw_value)
                except (ValueError, TypeError):
                    result[attr_name] = None
            else:
                result[attr_name] = None
        else:
            result[attr_name] = extract_nested_value(dictionary, spec)
    return result


def process_list_of_dicts_with_config(
    list_of_dicts: List[Dict],
    config: Dict[str, Union[List[str], Tuple[List[str], Callable]]],
) -> List[Dict[str, Any]]:
    """обработка списка словарей"""
    return [process_dictionary_with_config(item, config) for item in list_of_dicts]


def create_processor(
    config: Dict[str, Union[List[str], Tuple[List[str], Callable]]],
    list_processor: bool = False,
) -> Callable:
    """
    создает готовый процессор с предзагруженной конфигурацией.
    В случае, если list_processor == True,
    внутрь процессора подается process_list_of_dicts_with_config,
    иначе process_dictionary_with_config.
    """
    if list_processor:
        return lambda data_list: process_list_of_dicts_with_config(data_list, config)
    else:
        return lambda data_dict: process_dictionary_with_config(data_dict, config)
