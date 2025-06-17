class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def __repr__(self):
        if self.head is None:
            return "[]"
        else:
            last = self.head
            returnStr = f"[{last.data}]"
            while last.next:
                last = last.next
                returnStr += f"->[{last.data}]"
            returnStr+= "->X"
            return returnStr
    def __contains__(self,value):
        last = self.head #if value == last.data retun True
        if last is not None:
            return False
        else:
            while last is not None:
                if last.data == value:
                    return True
                else:
                    last = last.next
            return False
    def __len__(self):
        last = self.head
        length = 0
        while last is not None:
            last = last.next
            length+=1
        return length
    def append(self,value): #Complexity of O(N) Linear Time
        if self.head is  None:
            self.head = Node(value)
        else:
            last = self.head
            while last.next:                 # 2->
                last = last.next #Keep going till the last 
            last.next = Node(data=value)#Node.next = None
    def prepend(self,value):
        newHead = Node(data=value)
        newHead.next = self.head
        self.head = newHead
    def insert(self,value,index):
        if index == 0:
            LinkedList.prepend(value=value)
        else:
            if self.head is None:
                raise ValueError("Index Out of Bounds")
            else:
                last = self.head
                for i in range(index-1):
                    if last.next is None:
                        raise ValueError("Index Out of Bounds")
                    last = last.next
                newNode = Node(value)
                newNode.next = last.next
                last.next = newNode
    def delete(self,val):
        last = self.head
        if last is not None:
            if last.data == val:
                self.head = last.next
        else:
            while last.next:
                if last.next.data == val:
                    last.next = last.next.next
    def pop(self,index):
        if self.head is None:
            raise ValueError("Index Bounds Out Of Range")
        else:
            last = self.head
            for i in range(index-1):
                if last.next is None:
                    raise ValueError("Index Out oF f bounds")
                last = last.next
            if last.next is None:
                raise ValueError("Index Bounds out of range")
            else:
                last.next = last.next.next
    def print(self):
        if self.head is None:
            print("List is Empty")
        last = self.head            
        while last is not None:
            print(last.data)
            last = last.next



class BinaryTreee:
    def __init(self,data):
        self.right = None
        self.left = None
        self.data = data
    def insert(self,data):
        pass

    


ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(50)
ll.prepend(0)
ll.insert(index=4,value=40)
print(ll,"Before deletion")
ll.delete(val=30)
print(ll,"After deletion")