import re

def is_valid_string(s):
    pattern = r'^\{\{\{ARG_[a-zA-Z_]\w*\}\}\}$'
    return re.match(pattern, s) is not None

# Test examples:
strings_to_test = [
    "{{{ARG_example}}}",
    "{{{ARG_123invalid}}}",
    "{{{ARG_special!@#$%^}}}",
    "{{{ARG_starting_with_digit}}}",
    "{{{ARG_Valid_Word_123}}}",
]

for s in strings_to_test:
    print(f'{s}: {is_valid_string(s)}')
