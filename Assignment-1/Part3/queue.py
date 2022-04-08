
class Queue():
    def __init__(self):
        """
        Constructs a new queue
        """
        self._user_list = []

    def enqueue(self, num):
        """
        Adds an item to the queue
        """
        self._user_list.append(num)

    def dequeue(self) -> int:
        """
        Removes an item from the queue
        """
        if self.isEmpty():
            return None
        
        removed_item = self._user_list[0]
        self._user_list = self._user_list[1:]

        return removed_item

    def rear(self) -> int:
        """
        Returns an item at the end of the queue
        """
        return self._user_list[-1]

    def front(self) -> int:
        """
        Returns an item at the front of the queue
        """
        return self._user_list[0]

    def size(self) -> int:
        """
        Returns the size of the queue
        """
        return len(self._user_list)

    def isEmpty(self) -> bool:
        """
        Returns whether or not the queue is empty
        """
        if len(self._user_list) > 0:
            return False
        return True

if __name__ == "__main__":
    myQueue = Queue()
    myQueue.enqueue(1)
    myQueue.enqueue(2)
    myQueue.enqueue(3)
    print("Size of queue: ", end = "")
    print(myQueue.size())
    print("Front of queue:", myQueue.front())
    print("Rear of queue:", myQueue.rear())
    dequeued_item = myQueue.dequeue()
    print("Dequeued item:", dequeued_item)