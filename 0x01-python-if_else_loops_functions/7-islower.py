#!/usr/bin/python3
def islower(c):
    if ord('a') <= ord(c) <= ord('z'):
        return True
    else:
        return False


character = 'm'
print(f"Is {character} a lowercase? {islower(character)}")