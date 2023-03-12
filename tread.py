from time import sleep
from threading import Thread

class Task(Thread):
    def __init__(self, id, temp):
        Thread.__init__(self)
        self.id = id
        self.temp = temp
    
    def run(self):
        print(f"Start tread {self.id}")
        sleep(self.id)
        print(f"finish tread {self.id}")

def main():
    t1 = Task(11, 5)
    t2 = Task(12, 5)
    t1.start()#fa partire run
    t2.start()
    t1.join()
    t2.join()
    array = []
    for k in range(0, 10):
        print(k)
        array.append(Task(k, 5))
        array[k].start()

    #for k in range(0, 10):
        #t[k].join()
        #t[k].start()
    

if __name__ == "__main__":
    main()