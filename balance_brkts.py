from main import Stack


def check_balance(expr: str):
    list_opened = Stack()
    list_closed = Stack()
    brackets = {'(': ')', '[': ']', '{': '}'}
    for element in expr:
        if element in brackets.keys():
            list_opened.push(element)
        elif element in brackets.values():
            list_closed.push(element)
            if list_opened.size() < list_closed.size():
                return "Несбалансированно"
            if brackets[list_opened.peek()] != element:
                return "Несбалансированно"
            list_opened.pop()
            list_closed.pop()
    return "Сбалансированно"


# Пример сбалансированных последовательностей скобок:
brackets1 = '(((([{}]))))'
brackets2 = '[([])((([[[]]])))]{()}'
brackets3 = '{{[()]}}'

# Несбалансированные последовательности:
brackets4 = '}{}'
brackets5 = '{{[(])]}}'
brackets6 = '[[{())}]'

if __name__ == '__main__':
    print(check_balance(brackets1))
    print(check_balance(brackets2))
    print(check_balance(brackets3))
    print(check_balance(brackets4))
    print(check_balance(brackets5))
    print(check_balance(brackets6))

