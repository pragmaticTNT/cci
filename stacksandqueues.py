import helperfunction as h

## =========================
## ===> [STACK] Vanilla <===
## =========================
class Stack:
    def __init__(self, data=[]):
        self.data = data
        self.length = len(data)
        return
    def pop(self):
        item = self.data[-1]
        del self.data[-1]
        return item
    def push(self, item):
        self.data.append(item)
        return
    def peek(self):
        return self.data[-1]
    def isempty(self):
        return self.length == 0
    def __repr__(self):
        return str(self.data)

## ==============================
## ===> [STACK] Three-in-One <===
## ==============================
class Stack3In1(Stack):
    def __init__(self, data=[]):
        Stack.__init__(self, data)
        self.length = [0,0,0]
        self.lengthMax = 0
        return
    def pop(self, stackId=0):
        self.length[stackId] -= 1
        item = self.data[-1]
        del self.data[-1]
        return item
    def push(self, item, stackId=0):
        self.length[stackId] += 1
        if self.length > lengthMax:
            self.data.append(None)
            self.data.append(None)
            self.data.append(None)
        else:
            self.data[self.length1*3] = item
        return
    def peek(self, stackId=0):
        stackLen = self.length[stackId]-1
        return self.data[stackId+stackLen*3]

## =========================
## ===> [STACK] Minimum <===
## =========================
class StackMin:

## ===========================
## ===> [STACK] Of Plates <===
## ===========================
class StackPlates:

## =======================
## ===> [STACK] Queue <===
## =======================
class StackQueue:

## =========================
## ===> [STACK] Animals <===
## =========================
class StackAnimals:

## =========================
## ===> [QUEUE] Vanilla <===
## =========================
class Queue:
    def __init__(self, data=[]):
        self.data = data
        self.length = len(data)
        return


def main():
    print("\n[TEST] Vanilla-Stack")
    myStack = Stack()
    myStack.push(1)
    myStack.push(2)
    myStack.push(3)
    value = myStack.pop()
    print(f"I got {value}!")
    myStack.push(4)
    value = myStack.peek()
    print(f"I saw {value}!")
    print(f"Final state of stack: {myStack}")
    return

if __name__ == "__main__":
    main()
