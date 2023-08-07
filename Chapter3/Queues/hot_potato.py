#We will implement the hot_potato game using queue
from Queue import Queue
from random import randint

def hot_potato(name_list):
    sim_queue = Queue()

    for name in name_list:
        sim_queue.enqueue(name)

    while sim_queue.size() > 1:
        for i in range(randint(1, sim_queue.size())):
            sim_queue.enqueue(sim_queue.dequeue())
        
        sim_queue.dequeue()
    
    return sim_queue.dequeue()

if __name__ == "__main__":
    print(hot_potato(["Cepero", "Bonilla", "Martin", "Delgao", "Nore", "Rams", "Cava", "Nacho", "Arnau", "Gaxan", "Lailas"]))
