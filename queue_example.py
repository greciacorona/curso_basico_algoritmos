# Python program to 
# demonstrate implementation of 
# Queue (FIFO) using lists

queue = ["","","","",""]
size = 5
front = -1
rear = -1


def insert(value):
    global queue
    global size
    global front
    global rear
    if rear == len(queue)-1:
        print("Queue is full")
    else:
        if front == -1:
            front = 0
        rear += 1
        queue[rear] = value


def run():
    insert("x1")
    insert("x2")
    insert("x3")
    insert("x4")
    insert("x5")
    insert("x6")
    print(f'{queue} front: {front} rear: {rear}')
    
        
if __name__ == "__main__":
    run()