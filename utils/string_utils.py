from flask import abort
import re

def count_alphanumeric_filter(s):
    return len(list(filter(str.isalnum, s)))

def check_for_uuid(string):
    uuid_regex = r'^\S+$'
    return re.match(uuid_regex, string)