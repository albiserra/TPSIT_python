"""from time import sleep
from threading import Thread, Lock
import random

mutex = Lock()#creo il MUTEX
global buffer
buffer = 0

class ThreadProduttore(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        #global buffer
        buffer=0
        while True:
            if buffer == 0:
                mutex.acquire()
                buffer = random.randint(1,10)
                mutex.release()

class ThreadConsumatore(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        self.id = id

    def run(self):
        mutex.acquire()
        if self.id%2==0:
            if buffer>=1 and buffer<=5:
                mutex.acquire()
                print(f"thread {self.id} ha preso {buffer}")
                buffer = 0
                mutex.release()
        else:
            if buffer>=6 and buffer<=10:
                mutex.acquire()
                print(f"thread {self.id} ha preso {buffer}")
                buffer = 0
                mutex.release()

        mutex.release()

def main():
    prod = ThreadProduttore()
    prod.start()
    for k in range (1, 6):
        cons = ThreadConsumatore(k)
        cons.start()

if __name__ == "__main__":
    main()"""

######################################
#Un processo produttore genera in modo casuale (anche con ripetizioni) numeri da 1 a 10 (inclusi) e 
#li memorizza in un buffer condiviso che può contenere un solo numero alla volta. Due processi 
#consumatori concorrenti tentano di acquisire tali numeri soltanto dopo la loro produzione. 
#Uno dei due consumatori tenta di acquisire solo numeri da 1 a 5, l'altro solo numeri che vanno da 6 a 10. 
#Quando lo prendono settano il buffer (variabile) a 0 (zero)
#####################################


from time import sleep
from threading import Thread, Lock
import random

mutex = Lock()#creo il MUTEX
buffer = 0
continua = True #per far ciclare il produttore n volte e la stessa variabile fa ciclare i consumatori

class Produttore(Thread):

    def __init__(self, id):
        Thread.__init__(self)
        self.id = id
        

    def run(self):
        global buffer
        global continua
        i = 0
        #while(1):
        while (continua):
            if (buffer==0):
                mutex.acquire() 
                buffer = random.randint(1,10)
                print(f"Thread {self.id}: prodotto {buffer}")
                sleep(1)
                mutex.release() #rilascio MUTEX
                i+=1
                if (i==10):
                    continua = False
           

class Consumatore(Thread):

    def __init__(self, id, valoremin, valoremax):
        Thread.__init__(self)
        self.id = id
        self.valoremin = valoremin
        self.valoremax = valoremax
        self.valore_raccolto = 0
        
    def run(self):
        global buffer
        global continua
        #while(1):
        while (continua):
            if (buffer >= self.valoremin and buffer <= self.valoremax):
                mutex.acquire() 
                self.valore_raccolto += buffer
                print(f"Thread {self.id}: consumato {buffer} ed ho un totale di {self.valore_raccolto}")
                buffer = 0
                sleep(1)
                mutex.release() #rilascio MUTEX
                
       


#creo 5 thread e li faccio partire
consumatore_1 = Consumatore("Cons_1", 1, 5)
consumatore_2 = Consumatore("Cons_2", 6, 10)
produttore = Produttore("Produttore")

produttore.start()
consumatore_1.start()
consumatore_2.start()

produttore.join()
consumatore_1.join()
consumatore_2.join()