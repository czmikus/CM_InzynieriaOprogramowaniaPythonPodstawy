def check_parentheses(s: str) -> bool:
    stack = []

    for char in s:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if not stack:
                return False  # za dużo zamykających nawiasów
            stack.pop()

    return len(stack) == 0  # stos pusty = wszystkie nawiasy się zgadzają


# Przykładowe wywołanie:
if __name__ == "__main__":
    examples = [
        "( if ( zero ? x ) max (/ 1 x ))",
        "I told ( that its not ( yet ) done ). (42)",
        ":-)",
        "Czesc (o kurcze, chyba niechcacy zamkne ten nawias dwa razy))",
        "())(("
    ]
    for example in examples:
        print(f"{example} -> {check_parentheses(example)}")