class Stack():

    def __init__(self):
        self.list = []

    # проверка стека на пустоту. Метод возвращает True или False
    def isEmpty(self):
        return len(self.list) == 0

    # добавляет новый элемент на вершину стека. Метод ничего не возвращает
    def push(self, item):
        self.list.insert(0, item)

    # удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
    def pop(self):
        self.list.pop(0)
        return self.list[0]

    # возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
    def peek(self):
        return self.list[0]

    # возвращает количество элементов в стеке.
    def size(self):
        return len(self.list)


if __name__ == '__main__':
    f = Stack()
    # print(f.isEmpty())
    # f.push(1)
    # print(f.isEmpty())
    # f.push(2)
    # f.push(3)
    # f.push(4)
    # f.push(5)
    # print(f.list)
    # print(f.pop())
    # print(f.list)
    # print(f.peek())
    # print(f.size())






