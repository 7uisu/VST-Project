# templatetags/custom_tags.py
import logging
from django import template

register = template.Library()
logger = logging.getLogger(__name__)

@register.filter
def to(value, arg):
    """Usage, in template: {% for i in 1|to:5 %} ... {% endfor %}"""
    return range(value, arg + 1)

@register.filter
def get_last_value(value_list, key):
    """Get the last value of a specified key from a list of dictionaries"""
    if value_list:
        last_item = value_list[-1]
        return getattr(last_item, key, '-')
    return '-'  
@register.filter
def split(value, key):
    """Splits the value by the given key."""
    return value.split(key)

@register.filter
def get_item(dictionary, key):
    """Get an item from a dictionary"""
    return dictionary.get(key, '-')

@register.filter
def last_item_attr(responses_dict, attr_name):
    """Get an attribute from the last item in a dictionary of lists"""
    try:
        if isinstance(responses_dict, dict) and responses_dict:
            # Flatten the list of responses and get the last item
            all_responses = [item for sublist in responses_dict.values() for item in sublist]
            if all_responses:
                last_response = all_responses[-1]
                return getattr(last_response, attr_name, '-')
        logger.warning(f'Empty or invalid responses_dict: {responses_dict}, attr_name: {attr_name}')
        return '-'
    except Exception as e:
        logger.error(f'Error in last_item_attr filter: {e}')
        return '-'
