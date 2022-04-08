
class Stack():
    def __init__(self):
        """
        Constructs a new stack
        """
        self._user_list = []

    def push(self, num):
        """
        Pushes an integer on top of the stack
        """
        self._user_list.append(num)

    def pop(self) -> int:
        """
        Removes what is on top of the stack, 
        and returns that value to the caller
        """
        if self.isEmpty():
            return None
    
        top_num = self._user_list[-1]

        self._user_list = self._user_list[:-1]

        return top_num

    def top(self) -> int:
        """
        Looks at the top value of the stack and then returns it
        """
        if self.isEmpty():
            return None
        return self._user_list[-1]
        

    def isEmpty(self) -> bool:
        """
        Returns True if the list is empty, False otherwise
        """
        if len(self._user_list) == 0:
            return True
        return False

    def size(self) -> int:
        """
        Returns the size of the stack
        """
        return len(self._user_list)

if __name__ == "__main__":
    myStack = Stack()
    myStack.push(42)