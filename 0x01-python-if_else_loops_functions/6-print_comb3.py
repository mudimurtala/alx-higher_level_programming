#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    return str[:n] + str[n+1:]
  

def remove_char_at(str, n):
    if n < 0:
        str = str[:]
    else:
        str = str[:n] + str[n + 1:]
    return str