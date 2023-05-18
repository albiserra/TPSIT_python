from mimetypes import init
from threading import Thread, Lock

posti = 200
mutex = Lock()

class Cassa(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        self.id = id

    def run(self):
        global posti

        while posti > 0:
            mutex.acquire()
            if posti>0:
                biglietti = int(input(f"Inserire il numero di biglietti da acquistare alla cassa {self.id}: "))
                
                if biglietti > 0 and biglietti <= posti:
                    posti -= biglietti
                else:
                    print("Errore")
                
                print(f"I posti disponibili sono: {posti}")
            mutex.release()


def main():

    cassa1 = Cassa(1)
    cassa2 = Cassa(2)
    cassa3 = Cassa(3)
    cassa4 = Cassa(4)
    cassa5 = Cassa(5)
    cassa6 = Cassa(6)

    cassa1.start()
    cassa2.start()
    cassa3.start()
    cassa4.start()
    cassa5.start()
    cassa6.start()

    cassa1.join()
    cassa2.join()
    cassa3.join()
    cassa4.join()
    cassa5.join()
    cassa6.join()

    print("FINE THREAD")



if __name__ == "__main__":
    main()