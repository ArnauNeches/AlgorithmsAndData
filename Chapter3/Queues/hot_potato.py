#We will implement the hot_potato game using queue
from Queue import Queue

def hot_potato(name_list, num):
    sim_queue = Queue()

    for name in name_list:
        sim_queue.enqueue(name)

    while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())
        
        sim_queue.dequeue()
    
    return sim_queue.dequeue()

if __name__ == "__main__":
    print(hot_potato(["Cepero", "Bonilla", "Martin", "Delgao", "Nore", "Rams", "Cava", "Nacho", "Arnau", "Gaxan"], 6))
