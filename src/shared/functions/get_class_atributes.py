from typing import List, Any


def get_attribute_names(cls):
    attribute_names = []
    for attribute_name in dir(cls):
        if not attribute_name.startswith("__") or not attribute_name.endswith("__"):
            attribute_names.append(attribute_name)
    return attribute_names
