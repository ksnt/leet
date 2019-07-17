import time
class Foo:
    def __init__(self):
        self.flag = 0
        self.sleep_time = 0.000001
        
    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        while self.flag != 0:
           time.sleep(self.sleep_time) 
        printFirst()
        self.flag = 1

    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.flag != 1:
            time.sleep(self.sleep_time)
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.flag = 2

    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.flag != 2:
            time.sleep(self.sleep_time)
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
