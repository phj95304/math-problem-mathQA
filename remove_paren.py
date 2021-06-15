import sys
text = sys.argv[1]

def remove_brackets(term):
    a = 0
    while True:
        # Find opening bracket
        try:
            a = term.index("(", a)
        except ValueError:
            # No (more) opening brackets found
            break
        # Find corresponding closing bracket
        b = a
        while True:
            b = term.index(")", b + 1)
            if term[a + 1:b].count("(") == term[a + 1:b].count(")"):
                break
        # Assemble new term by removing current pair of brackets
        new_term = term[:a] + term[a + 1:b] + term[b + 1:]
        # If new term produces a different value, keep term as it is and try with the next pair of brackets
        if eval(term) != eval(new_term):
            a += 1
            continue
        # Adopt new term
        term = new_term
    return term

print(remove_brackets(text))
