# 1. Смоделируйте ситуацию обслуживания клиентов в банке. Клиенты, случайным образом помещаются
# в одну из M очередей обслуживания. Случайным образом выбирается одна из очередей, и клиент обслуживается
# (выбывает из очереди). При каждой операции указывайте номер добавленного клиента,
# номер обслуженного клиента, и состояние очередей.
from random import randint
import threading

# Очередь клиентов
M = []
for i in range(0, 102):
    alphabet = "АБВГДЕЖЗ"
    M.append(alphabet[randint(0, 7)] + str(randint(1, 999)))


def clients(massive, number):
    people = 33
    for client in massive:
        print(' Клиент {} подошел к окну с номером [{}]'.format(client, number), sep= '/n')
        print(' Клиент {} покинул окно с номером [{}]'.format(client, number), sep= '/n')
        print(' Окно {}: колличество клиентов = {}'.format(number, people), sep='/n')
        people -= 1

# Задаем потоки
window_1 = threading.Thread(target=clients, args=(M[0: 34], '1'))
window_2 = threading.Thread(target=clients, args=(M[34: 68], '2'))
window_3 = threading.Thread(target=clients, args=(M[68: 102], '3'))

# Работа с потоками
window_1.start()
window_2.start()
window_3.start()
window_1.join()
window_2.join()
window_3.join()
