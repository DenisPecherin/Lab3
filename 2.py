# 2. Реализуйте АТД «Очередь с приоритетами».
# а) с приоритетным включением;
# б) с приоритетным исключением.
class QueuePriorityIn:  # Очередь с приоритетным включением
    def __init__(self, m):  # конструктор с параметром m - максимальной длиной очереди
        self.MaxQueueLength = m
        self.Wait = [0] * m  # список с элементами очереди
        self.Pri = [0] * m  # список с приоритетами элементов очереди
        self.QueueLength = 0  # длина очереди

    def Show(self):  # вывод очереди
        for i in range(0, self.QueueLength):
            print(str(self.Wait[i]) + " - " + str(self.Pri[i]))

    def isFull(self):  # проверка полноты очереди
        return self.QueueLength == self.MaxQueueLength

    def Add(self, elem, pri):  # добавление элемента в очередь с приоритетом
        if not self.isFull():  # если в очереди есть место
            self.Wait[self.QueueLength] = elem  # добавить новый элемент
            self.Pri[self.QueueLength] = pri  # с приоритетом
            self.QueueLength += 1  # и увеличить длину очереди на 1
            while True:  # сортируем список элементов по их приоритетам (пузырьковая сортировка)
                swapped = False
                for i in range(0, self.QueueLength - 1):
                    if self.Pri[i] < self.Pri[i + 1]:
                        self.Pri[i], self.Pri[i + 1] = self.Pri[i + 1], self.Pri[i]
                        self.Wait[i], self.Wait[i + 1] = self.Wait[i + 1], self.Wait[i]
                        swapped = True
                if not swapped:
                    break

    def Extract(self):  # извлечение элемента с наибольшим приоритетом из очереди
        if self.QueueLength != 0:  # если очередь не пуста
            answer = self.Wait[0]  # сохранить первый элемент в переменную
            for i in range(0, self.QueueLength):  # сдвинуть все элементы
                self.Wait[i] = self.Wait[i + 1]
                self.Pri[i] = self.Pri[i + 1]
            self.QueueLength = -1  # уменьшить текущую длину очереди на 1
            return answer  # вернуть найденный элемент


class QueuePriorityEx:  # Очередь с приоритетным исключением
    def __init__(self, m):  # m - максимальная длина очереди
        self.MaxQueueLength = m
        self.Wait = [0] * m  # список с элементами очереди
        self.Pri = [0] * m  # список с приоритетами элементов очереди
        self.QueueLength = 0  # длина очереди

    def Show(self):  # вывод очереди
        for i in range(0, self.QueueLength):
            print(str(self.Wait[i]) + " - " + str(self.Pri[i]))

    def isFull(self):  # проверка полноты очереди
        return self.QueueLength == self.MaxQueueLength

    def Add(self, elem, pri):  # добавление элемента в очередь с приоритетом
        if not self.isFull():  # если в очереди есть место
            self.Wait[self.QueueLength] = elem  # добавить новый элемент
            self.Pri[self.QueueLength] = pri  # с приоритетом
            self.QueueLength += 1  # и увеличить длину очереди на 1

    def Extract(self):  # извлечение элемента с наибольшим приоритетом из очереди
        if self.QueueLength != 0:  # если очередь не пуста
            pos_max = self.Pri.index(max(self.Pri))  # найти индекс элемента с максимальный приоритетом
            answer = self.Wait[pos_max]  # сохранить его в переменную
            for i in range(pos_max, self.QueueLength):  # сдвинуть все элементы
                self.Wait[i] = self.Wait[i + 1]
                self.Pri[i] = self.Pri[i + 1]
            self.QueueLength = -1  # уменьшить текущую длину очереди на 1
            return answer  # вернуть найденный элемент

# Очередь с приоритетным включением
queuea = QueuePriorityIn(5)
queuea.Add(4, 42)  # добавление
queuea.Add(8, 2)
queuea.Add(2, 38)
queuea.Add(6, 59)
queuea.Show()  # вывод
print("Извлечен элемент " + str(queuea.Extract()))
# Очередь с приоритетным исключением
queueb = QueuePriorityEx(5)
queueb.Add(4, 50)
queueb.Add(6, 49)
queueb.Show()
print("Извлечен элемент " + str(queueb.Extract()))
