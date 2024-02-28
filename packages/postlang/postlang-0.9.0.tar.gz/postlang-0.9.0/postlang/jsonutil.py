import json


def is_json_convertible(obj):
    try:
        json.dumps(obj)
        return True
    except (TypeError, OverflowError):
        return False


def json_convertible(obj):
    """
    Convert any Python object into an object that can be serialized to JSON.
    This function handles dictionaries, lists, and objects with custom conversion methods,
    applying conversions recursively.
    """

    if is_json_convertible(obj):
        return obj

    if isinstance(obj, dict):
        return {key: json_convertible(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [json_convertible(item) for item in obj]
    elif hasattr(obj, "to_json"):
        try:
            return obj.to_json()
        except TypeError:
            return str(obj)
    elif hasattr(obj, "to_dict"):
        try:
            return json_convertible(obj.to_dict())
        except TypeError:
            return str(obj)
    else:
        return str(obj)
