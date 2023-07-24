from typing import Optional

BALANCE_DICT = {
    '(': ')',
    '[': ']',
    '{': '}'
}


class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self) -> bool:
        """Проверка пуст ли наш список"""
        return self.size() == 0

    def push(self, item: str) -> None:
        """Добавление элемента в конец списка"""
        self.data.append(item)

    def pop(self):
        """Удаление элемента из конца списка"""
        if self.is_empty():
            return None
        return self.data.pop()

    def peek(self) -> Optional[str]:
        """Получение последнего элемента из списка"""
        if self.is_empty():
            return None
        return self.data[-1]

    def size(self) -> int:
        """Получение длины списка"""
        return len(self.data)


def check_balance(string: str) -> bool:
    """Проверка строки на сбалансированность скобок"""
    stack = Stack()
    for item in string:
        if item in BALANCE_DICT:
            stack.push(item)
        elif BALANCE_DICT.get(stack.peek()) == item:
            stack.pop()
        else:
            return False
    return stack.is_empty()


if __name__ == '__main__':
    our_list = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}',
                '{{[(])]}}', '[[{())}]]']

    for string in our_list:
        print(f'{string} - {check_balance(string)}')
