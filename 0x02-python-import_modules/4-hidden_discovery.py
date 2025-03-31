#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    items = dir(hidden_4)

    items = sorted(items)
    for i in items:
        if i[:2] != "__":
            print(i)
