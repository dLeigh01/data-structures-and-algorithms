import re
from data_structures.stack import Stack


def multi_bracket_validation(text):
    clean_text = list(re.findall('\{|\[|\(|\}|\]|\)', text))
    stack = Stack()
    while clean_text:
        if clean_text[0] == '{' or clean_text[0] == '(' or clean_text[0] == '[':
            stack.push(clean_text.pop(0))
            continue
        if stack.top is None:
            return False
        if stack.top:
            if stack.top.value == char_match(clean_text[0]):
                clean_text.pop(0)
                stack.pop()
                continue
            return False
    return True

def char_match(char):
    if char == '}':
        return '{'
    if char == ']':
        return '['
    if char == ')':
        return '('
