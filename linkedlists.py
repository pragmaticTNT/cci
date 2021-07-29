import helperfunction as h

## ====================================
## ===> Linked List Implementation <===
## ====================================
class Node:
    def __init__(self, data):
        self.data = data
        self.visited = False
        self.child = None
        return

class LinkedList:
    def __init__(self, listData=[]):
        self.size = len(listData)
        self.head = None
        for i in range(self.size-1, -1, -1):
            newNode = Node(listData[i])
            newNode.child = self.head
            self.head = newNode
        return

    def __repr__(self):
        pt = self.head
        linkedListStr = ""
        while pt:
            dataStr = str(pt.data)
            if pt.child is not None:
                linkedListStr += dataStr + " -> "
            else:
                linkedListStr += dataStr
            pt = pt.child
        return linkedListStr

    def __len__(self):
        return self.size

    ## ==================================
    ## ===> QUESTION IMPLEMENTATIONS <===
    ## ==================================
    def removedups(self):
        current = self.head
        parent = current
        while current and current == parent:
            currData = current.data
            runner = current.child
            runner = self.__nodewithdata(runner, currData)
            if runner:
                current = current.child
                self.head = current
                parent = current
            else:
                current = current.child
        while current:
            currData = current.data
            dupNode = current.child
            dupNode = self.__nodewithdata(dupNode, currData)
            if dupNode:
                parent.child = current.child
                current = current.child
            else:
                parent = current
                current = current.child
        return

    def __nodewithdata(self, node, data):
        nextNode = node
        while nextNode:
            if nextNode.data == data:
                return nextNode
            nextNode = nextNode.child
        return nextNode

    def returnktolast(self, k):
        if k > self.size:
            return "DOES NOT EXIST"
        counter = self.size - k
        nodePtr = self.head
        while counter:
            nodePtr = nodePtr.child
            counter -= 1
        return nodePtr.data

    def deletemiddle(self):
        head = self.head
        if head:
            middle = head.child
            if middle.child is not None:
                head.child = middle.child
                return middle.data
        return

    def partition(self, value):
        larger = self.head
        while larger:
            if larger.data >= value:
                smaller = larger.child
                while smaller and smaller.data >= value:
                    smaller = smaller.child
                if smaller:
                    smaller.data, larger.data = larger.data, smaller.data
            larger = larger.child
        return

    def palindrome(self):
        middle = self.size//2
        [isPal, nodePtr] = self.__palhelper(self.head, middle)
        return isPal

    def __palhelper(self, currentPtr, index):
        parity = (self.size+1) % 2
        data = currentPtr.data
        nextPtr = currentPtr.child
        dataNext = nextPtr.data
        if index == parity:
            if parity:
                return [data == dataNext, nextPtr]
            else:
                return [True, currentPtr]
        [match, otherPtr] = self.__palhelper(nextPtr, index-1)
        if not match:
            return [False, None]
        otherPtr = otherPtr.child
        dataOther = otherPtr.data
        return [data == dataOther, otherPtr]

    def gettail(self):
        head = self.head
        while head.child:
            head = head.child
        return head

def sumlistl(list1, list2):
    if len(list1) > len(list2):
        list1, list2 = list2, list1
    head1 = list1.head
    head2 = list2.head
    carry = 0
    sumArray = []
    while head2:
        if head1:
            sumDigit = head1.data + head2.data + carry
            head1 = head1.child
        else:
            sumDigit = head2.data + carry
        digit = sumDigit % 10
        carry = sumDigit // 10
        sumArray.append(digit)
        head2 = head2.child
    sumList = LinkedList(sumArray)
    return sumList

def sumlistb(list1, list2):
    if len(list1) > len(list2):
        list1, list2 = list2, list1
    nlist1 = len(list1)
    nlist2 = len(list2)
    head1 = list1.head
    head2 = list2.head
    sumArray = []
    carry = helpsumlistb(sumArray, head1, head2, nlist1, nlist2)
    if carry:
        sumArray.append(carry)
    sumArray.reverse()
    sumList = LinkedList(sumArray)
    return sumList

## Implicitly assume that List2 is the longer list
def helpsumlistb(sumArray, node1, node2, nList1, nList2):
    if nList1 == nList2:
        sumDigit = 0
        if nList1 > 1:
            next1 = node1.child
            next2 = node2.child
            carry = helpsumlistb(sumArray, next1, next2, nList1-1, nList2-1)
            sumDigit += carry
        sumDigit += node1.data + node2.data
    else:
        next2 = node2.child
        carry = helpsumlistb(sumArray, node1, next2, nList1, nList2-1)
        sumDigit = node2.data + carry
    digit = sumDigit % 10
    carry = sumDigit // 10
    sumArray.append(digit)
    return carry

def loopdetection(ll):
    hasLoop = False
    walk = ll.head
    run = ll.head
    nList = len(ll)
    for i in range(nList+1):
        walk = walk.child
        run = run.child
        if run is None or run.child is None:
            break
        run = run.child
        if walk == run:
            hasLoop = True
            break
    if hasLoop:
        start = ll.head
        while start != walk:
            start = start.child
            walk = walk.child
    return [hasLoop, walk]

def main():
    folderName = "linkedlists/"
    h.FOLDERNAME = folderName

    print("[TEST] Linked List Data Structure")
    listEntries = [i for i in range(10)]
    myList = LinkedList(listEntries)
    print(myList)

    print("\n[TEST] 2.1 Remove Dups")
    dataRemoveDups = h.readfile("testRemoveDups", 0)
    for listData in dataRemoveDups:
        currList = listData.split()
        ll = LinkedList(currList)
        print(f"Bef: {ll}")
        ll.removedups()
        print(f"Aft: {ll}")

    print("\n[TEST] 2.2 Return Kth to Last")
    dataReturnKth = h.readfile("testReturnKthToLast", 0)
    for listData in dataReturnKth:
        [listStr, k] = listData.split(", ")
        k = int(k)
        listArray = listStr.split()
        ll = LinkedList(listArray)
        print(ll)
        kToLastValue = ll.returnktolast(k)
        ##print("The {} to last value is: {}".format(k, kToLastValue))
        print(f"The {k} to last value is: {kToLastValue}")

    print("\n[TEST] 2.3 Delete Middle Node")
    dataDeleteMiddle = h.readfile("testDeleteMiddle", 0)
    for listData in dataDeleteMiddle:
        listArray = listData.split()
        ll = LinkedList(listArray)
        print(f"Bef: {ll}")
        ll.deletemiddle()
        print(f"Aft: {ll}")

    print("\n[TEST] 2.4 Partition")
    dataPartition = h.readfile("testPartition", 0)
    for listData in dataPartition:
        [listArray, partitionVal] = listData.split(", ")
        partitionVal = int(partitionVal)
        listArray = listArray.split()
        listArray = [int(val) for val in listArray]
        ll = LinkedList(listArray)
        print(f"Bef: {ll}")
        print(f"Partition around {partitionVal}")
        ll.partition(partitionVal)
        print(f"Aft: {ll}\n---\n")

    print("\n[TEST] 2.5.a Sum Lists - Little Endian")
    dataSumListL = h.readfile("testSumListLittleEnd", 0)
    for pair in dataSumListL:
        [numStr1, numStr2] = pair.split(", ")
        numArray1 = [int(i) for i in numStr1.split()]
        numArray2 = [int(i) for i in numStr2.split()]
        numList1 = LinkedList(numArray1)
        numList2 = LinkedList(numArray2)
        sumList = sumlistl(numList1, numList2)
        print(f"{numList1} and {numList2} sum to {sumList}")

    print("\n[TEST] 2.5.b Sum Lists - Big Endian")
    dataSumListB = h.readfile("testSumListLittleEnd", 0)
    for pair in dataSumListB:
        [numStr1, numStr2] = pair.split(", ")
        numArray1 = [int(i) for i in numStr1.split()]
        numArray2 = [int(i) for i in numStr2.split()]
        numList1 = LinkedList(numArray1)
        numList2 = LinkedList(numArray2)
        sumList = sumlistb(numList1, numList2)
        print(f"{numList1} and {numList2} sum to {sumList}")

    print("\n[TEST] 2.6 Palindrome")
    dataPalindrome = h.readfile("testPalindrome", 0)
    for listData in dataPalindrome:
        listArray = listData.split()
        ll = LinkedList(listArray)
        print(ll)
        isPal = ll.palindrome()
        isPal = h.booltostr(isPal)
        print(f"Is this a palindrome? {isPal}")

    ## ---> Implicitly test this in the next question
    ##print("\n[TEST] 2.7 Intersection")

    print("\n[TEST] 2.8 Loop Detection")
    ## ---> Adding a loop
    listLen = 10
    startLoop = 8
    ll = LinkedList([i for i in range(listLen)])
    head = ll.head
    tail = ll.gettail()
    for i in range(startLoop):
        head = head.child
    tail.child = head

    [hasLoop, loopHead] = loopdetection(ll)
    print(f"Does list2 have a loop? {hasLoop}")
    print(f"The start of the loop is at: {loopHead.data}")
    return

if __name__ == "__main__":
    main()
