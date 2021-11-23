import copy

# STACK CLASS DEFINITION


class Stack:
    MAX = 500

    def __init__(self, stack):
        self._stack = list(stack)

    def isEmpty(self):
        if len(self._stack) == 0:
            return True
        else:
            return False

    def isFull(self):
        if len(self._stack) == MAX:
            return True
        else:
            return False

    def pop(self):
        if not self.isEmpty():
            self._stack.pop()

    def push(self, elem):
        if not self.isFull():
            self._stack.append(elem)

    def peek(self):
        if not self.isEmpty():
            return self._stack[-1]
        else:
            return None

    def len(self):
        return len(self._stack)


# QUEUE CLASS DEFINITION
class Queue:
    MAX = 500

    def __init__(self, queue):
        self._queue = list(queue)

    def isEmpty(self):
        if len(self._queue) == 0:
            return True
        else:
            return False

    def isFull(self):
        if len(self._queue) == MAX:
            return True
        else:
            return False

    def dequeue(self):
        if not self.isEmpty():
            self._queue.pop(0)

    def enqueue(self, elem):
        if not self.isEmpty():
            self._queue.append(elem)

    def peek(self):
        if not self.isEmpty():
            return self._queue[0]
        else:
            return None

    def len(self):
        return len(self._queue)


def Simulate_Sandwitch_for_Students(Students, Sandwitch):
    """
    (list of integers, list of integers) -> (int)
    Returns the number of students that were unable to eat.
    >>> Simulate_Sandwitch_for_Students([1,1,0,0], [0,1,0,1])
    0
    >>> Simulate_Sandwitch_for_Students([1,1,1,0,0,1], [1,0,0,0,1,1])
    3
    """

    Sandwitch.reverse()
    stdntQueue = Queue(Students)
    sandwichStack = Stack(Sandwitch)

    i = 0
    repeatNum = 0  # Saving the array repeation number over succesive iterations
    while not stdntQueue.isEmpty():
        oldQueue = copy.deepcopy(stdntQueue._queue)  # Save old student queue

        sw = sandwichStack.peek()
        st = stdntQueue.peek()

        if sw == st:
            stdntQueue.dequeue()
            sandwichStack.pop()
            if i != 0:
                if stdntQueue._queue == oldQueue:
                    repeatNum += 1  # Increase repeatNum as student queue didn't change
                else:
                    repeatNum = 0  # Reset repeatNum to 0 if student queue changes

            if stdntQueue.len() == repeatNum:  # If the student has cycled the queue and
                break  # yet the queue hasnt changed, we halt
        else:
            stdntQueue.dequeue()
            stdntQueue.enqueue(st)

            if i != 0:
                if stdntQueue._queue == oldQueue:
                    repeatNum += 1  # Increase repeatNum as student queue didn't change
                else:
                    repeatNum = 0  # Reset repeatNum to 0 if student queue changes

            if stdntQueue.len() == repeatNum:  # If the student has cycled the queue and
                break  # yet the queue hasnt changed, we halt

        i += 1

    output = stdntQueue.len()
    return output


print(Simulate_Sandwitch_for_Students([1, 1, 0, 0], [0, 1, 0, 1]))
print(Simulate_Sandwitch_for_Students([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))
