from threading import Thread, Lock
import random
from time import sleep

posti_liberi = 12#posti liberi nel parcheggio

mutex = Lock()#dichiaro il mutex

class auto(Thread):#classe del thread dell'auto
    def __init__(self, id):
        Thread.__init__(self)#iniziaizzo il thread
        self.id = id#ogni macchina ha un id per riconoscerla

    def run(self):
        global posti_liberi#dutilizzo globale posti liberi per poterla modificare
        tmp = random.randint(1, 5)#tempo di permanenza auto
        entrato = False#var per capire se l'auto è entrata o no
        while entrato == False:#ciclo se l'auto non è entrata
            mutex.acquire()#blocco per evitare che venga eseguito il controllo in contemporanea du più auto
            if posti_liberi > 0:#controllo se ci sono posti liberi, se ce ne sono entra
                posti_liberi -= 1#diminuisco i posti liberi
                entrato = True#setto la variabile a true per uscire dal while
                print(f"entra auto {self.id}, posti liberi: {posti_liberi} su 12")
            mutex.release()
        sleep(tmp)#aspetto il tempo necessario
        mutex.acquire()#blocco per cambiare posti liberi
        posti_liberi += 1#aumento perchè esce la macchina
        print(f"esce auto {self.id}, posti liberi: {posti_liberi} su 12")
        mutex.release()


def main():#utilizzo il main thread come parcheggio
    n_auto = random.randint(15, 21)#numero di auto
    print(f"numero auto: {n_auto}")
    array_Auto = []#creo un array di auto
    for i in range(0, n_auto):#dichiaro il numero di auto estratto e li faccio partire
        array_Auto.append(auto(i))#aggiungo l'auto all'array e avvio il thread
        array_Auto[i].start()

    for i in range(1, n_auto):
        array_Auto[i].join()#aspetto che ogni thread finisca

if __name__ == "__main__":
    main()