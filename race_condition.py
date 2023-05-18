import threading
saldo = 100

mutex = threading.Lock()

class Deposita(threading.Thread):
    def __init__(self):
        super().__init__()
    
    def run(self):
        global saldo
        for _ in range (1000000):
            mutex.acquire()
            saldo = saldo + 10
            mutex.release()

class Preleva(threading.Thread):
    def __init__(self):
        super().__init__()
    
    def run(self):
        global saldo
        for _ in range (1000000):
            mutex.acquire()
            saldo = saldo - 10
            mutex.release()


def main():
    #istanze oggetti thread
    alice = Deposita()
    bob = Preleva()

    #esecuzione thread
    alice.start()
    bob.start()
    print("aspecto la fine dei thread")
    #join thread
    alice.join()
    bob.join()

    print(f"il saldo è {saldo}")

if __name__ == "__main__":
    main()