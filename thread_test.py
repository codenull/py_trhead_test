from threading import Thread
from math import sin, cos
from array import array


class MyThread(Thread):

    def __init__(self, name, array):
        Thread.__init__(self)
        self.name = name
        self.array = array

    def run(self):
        for i, val in self.array:
            self.array[i] = self.calc(val, i)

    def calc(self, value, i):
        result = (value *
                  sin(0.2 + i / 5.0) *
                  cos(0.2 + i / 5.0) *
                  cos(0.4 + i / 2.0));
        return result


def create_array(array_len):
    return array('f', [1]) * array_len


def main():

    arr = create_array(1000)

    print("Start")
    print(create_array(10))


if __name__ == '__main__':
    main()

