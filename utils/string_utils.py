from flask import abort
import re

def count_alphanumeric_filter(s):
    return len(list(filter(str.isalnum, s)))

def check_for_uuid(string):
    uuid_regex = r'^\S+$'
    if not re.match(uuid_regex, string):
        abort(404, description="No receipt found for that id")