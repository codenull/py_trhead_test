from threading import Thread
from math import sin, cos
from array import array


class MyThread(Thread):

    def __init__(self, name, array, offset):
        Thread.__init__(self)
        self.name = name
        self.array = array
        self.offset = offset
        self.start()

    def run(self):
        for i, val in enumerate(self.array):
            self.array[i] = self.calc(val, (i + self.offset))

    def calc(self, value, i):
        result = (value *
                  sin(0.2 + i / 5.0) *
                  cos(0.2 + i / 5.0) *
                  cos(0.4 + i / 2.0));
        return result


def create_array(array_len):
    return array('f', [1]) * array_len


def make_calc(array_len, thread_count):
    if array_len % thread_count != 0:
        raise Exception('Невозможно разделить массив. Размер массив: {}. Количество потокв: {}'.format(array_len, thread_count))

    size  = int(array_len/thread_count)
    val_array = create_array(array_len)

    # Запуск расчетов.
    thread_list = []
    for i in range(thread_count):
        offset = i * size
        cur_array = val_array[offset: (i+1) * size]
        thread = MyThread("Thread #" + str(i), cur_array, offset)
        thread_list.append(thread)

    # Ожидаем завершение расчетов.
    for thread in thread_list:
        thread.join()

    # Собираем результат.
    result = array('f', [])
    for thread in thread_list:
        result += thread.array

    return result




def main():
    print("Start")
    make_calc(100, 2)
    make_calc(1000, 4)



if __name__ == '__main__':
    main()

