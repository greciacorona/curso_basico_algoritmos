# Python program to 
# demonstrate implementation of 
# Queue (FIFO) using lists
# with input

queue = ["","","","",""]
front = -1
rear = -1


def insert(value):
    global queue, front, rear
    # global front
    # global rear
    if rear == len(queue)-1:
        print("Queue is full")
    else:
        if front == -1:
            front = 0
        rear += 1
        queue[rear] = value
        print(f"{value} added")


def extract():
    global queue, front, rear
    # global front
    # global rear
    if front == -1:
        print("Queue is empty")
    elif front > rear:
        print("Queue is empty, there's nothing to delete")
        front = rear = -1
    elif front == rear:
        print(f"{queue[front]} was deleted")
        queue[front] = ""
        print("Queue is now empty")
        front = rear = -1
    else:
        print(f"{queue[front]} was deleted")
        queue[front] = ""
        front += 1
    

def run():
    option = 0
    while option != 4:
        menu = """
            Welcome, choose an option:
            1 - Add a customer
            2 - Delete the last customer
            3 - See the queue
            4 - Exit
            """

        option = int(input(menu))

        if option == 1:
            value = input("Client's name: ")
            insert(value)
        elif option == 2:
            extract()
        elif option == 3:
            print(f"{queue} front: {front} rear: {rear}\n")   
        elif option == 4:
            print("Goodbye")    
            break
        else:
            print("Incorrect Option")


if __name__ == "__main__":
    run()
