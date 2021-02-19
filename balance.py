from interv import Stack


def is_balanced(string):
    opening = '([{'
    closing = ')]}'
    brackets_map = {')': '(', ']': '[', '}': '{'}
    stack = Stack()
    for bracket in string:
        if bracket in opening:
            stack.push(bracket)  # добавляем скобку на вершину стека
        elif bracket in closing:
            if stack.isEmpty():  # если стек пуст, но у нас идет закрывающая скобка
                return False
            open_bracket = stack.peek()
            if open_bracket != brackets_map.get(bracket):
                '''Если на вершине стека открывающая скобка
                 не соответствует такой же закрывающей,
                 строка со скобками несбалансированна
                 '''
                return False
            else:
                '''Удаляем открывающую скобку на вершине стека,
                если она соответствует зарывающей, проводим проверку дальше
                '''
                stack.list.pop(0)
    return stack.isEmpty()


if __name__ == '__main__':
    string = '[([])]{()}{{[()]}}'
    print("Сбалансировано" if is_balanced(string) == True
          else "Несбалансировано")

    '''Пример сбалансированных последовательностей скобок:
    (((([{}]))))
    [([])((([[[]]])))]{()}
    {{[()]}}
   
    Несбалансированные последовательности:
    }{}
    {{[(])]}}
    [[{())}]
    '''