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
    arrayPari = []
    arrayDispari = []
    for k in range(0, 10):
        print(k)
        if k%2 == 0:
            arrayPari.append(Task(k, 5))
            arrayPari[int(k/2)].start()
        if k%2 == 1:
            arrayDispari.append(Task(k, 5))
            arrayDispari[int(round(k/2)-1)].start()

if __name__ == "__main__":
    main()