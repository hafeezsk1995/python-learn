from threading import *
from time import sleep
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")  
            sleep(1)          

t1 = Hello()
t2 = Hi()

t1.start()  # if you want to use start method in class should have run method
sleep(0.2)
t2.start()            

t1.join()  # this says let me complete t1
t2.join() # this says let me complete t2
print("bye")