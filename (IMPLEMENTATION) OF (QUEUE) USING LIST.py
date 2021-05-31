# QUEUE IMPLEMENTATION USING LIST, OPERATIONS LIKE:- (enqueue, dequeue, display, isempty, front/top/peek)
# follw -----> FIFO/LILO


#Define a class
class queue_maker() :
    def __init__(self) :
        self.queue = []

    def enqueue(self,ele) :
        (self.queue).append(ele)

    def dequeue(self) :
        #First Element is removed
        #pop(index),
        #index = 0 for first element of queue-->[]
        (self.queue).pop(0)

    def display(self) :
        print(self.queue)

    def isempty(self) :
        count = 0
        for ele in self.queue :
            count += 1

        if count == 0 :
            print("Empty Queue!")
        else :
            print("Not Empty")

    def peek(self) :
        #The very first element of queue(list) is displayed
        print(self.queue[0])


#Making an instance of class
new_queue = queue_maker()


#MAIN CODE :- TAKING INPUT FROM USER AT RUNTIME (LIKE:- OPERATION,ELEMENT,WANT TO PERFORM MORE OPERATIONS OR NOT)
repeat = True
while repeat == True :

    #Taking input for Type of operation
    print("Enter Operation you want to perform from (enqueue,dequeue,display,isempty,peek/top/front")
    oper = input()
          
    if oper == "enqueue" :
          print("enter element to enter into queue")
          ele_enqueue = input()
          new_queue.enqueue(ele_enqueue)

    elif oper == 'dequeue' :
        new_queue.dequeue()

    elif oper == 'display':
        new_queue.display()

    elif oper == 'isempty' :
        new_queue.isempty()

    elif oper == 'peek' or oper == 'top' or oper == 'front' :
        new_queue.peek()

    #ASK, THAT IF YOU WANT TO PERFORM MORE OPERATIIONS OR NOT 
    print("WANT TO PERFORM MORE OPERATION ?")
    repe_check = input()
    if repe_check == 'yes' or repe_check =='y' :
        pass
    else :
        repeat = False
