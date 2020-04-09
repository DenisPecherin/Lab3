# 3. Напишите программу для решения задачи о Ханойской башне без использования рекурсии.
class Tower: #класс объектов, хранящих внутренние состояния башен
    def __init__(self, n, one, next, help, step):
        self.n = n #количество дисков
        self.one = one #номер стержня, с которого выполняется перемещение
        self.next = next #номер стержня, на который выполняется перемещение
        self.help = help #номер вспомогательного стержня
        self.step = step #позиция, на которой находится выполнение алгоритма

def tower(n, one, next, help):
    stack = [] #создаем стек
    state = Tower(n, one, next, help, 0)
    sum = 0
    stack.append(state) #добавляем состояние в стек
    while len(stack) > 0: #пока стек не пуст
        state = stack[-1] #берем последний добавленный элемент стека
        if state.step==0:
            if state.n == 0: #если число дисков равно нулю
                stack.pop() #то удалить рассматриваемый элемент стека
            else:
                state.step+=1 #иначе перейти к следующему шагу

                newState = Tower(state.n-1, state.one, state.help, state.next, 0) #переложить n-1 дисков на вспомогательный, используя конечный
                stack.append(newState) #добавить новое состояние в стек
            continue
        if state.step==1:

            print("с " + str(state.one) + " перемещаем диск на " + str(state.next)) #вывести данные о перемещении диска
            state.step+=1
            newState = Tower(state.n-1, state.help, state.next, state.one, 0) #переложить n-1 дисков со вспомогательного стержня на конечный, используя начальный
            stack.append(newState)#добавить новое состояние в стек
            continue
        if state.step==2:
            sum += 1
            stack.pop() #удалить рассматриваемый элемент стека
            continue
    print("Перемещений = " + str(sum))

tower(3, 1, 2, 3)
