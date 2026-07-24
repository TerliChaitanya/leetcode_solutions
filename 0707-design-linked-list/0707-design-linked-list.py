class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
class MyLinkedList:

    def __init__(self):
        self.head=None
        self.size=0

    def get(self, index: int) -> int:
        if index<0 or index>=self.size:
            return -1
        i=0
        temp=self.head
        while temp:
            if index==i:
                return temp.val
            i+=1
            temp=temp.next
        return -1

    def addAtHead(self, val: int) -> None:
        node=Node(val)
        node.next=self.head
        self.head=node
        self.size+=1

    def addAtTail(self, val: int) -> None:
        node=Node(val)
        if self.head is None:
            self.head=node
            self.size+=1
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=node
        self.size+=1
    def addAtIndex(self, index: int, val: int) -> None:
        if index<0:
            self.addAtHead(val)
            return
        if index>self.size:
            return 
        temp=self.head
        if index==0:
            self.addAtHead(val)
            return
        for _ in range(index-1):
            temp=temp.next
        node=Node(val)
        node.next=temp.next
        temp.next=node
        self.size+=1
    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=self.size:
            return 
        temp=self.head
        if index==0:
            self.head=self.head.next
        else:
            for _ in range(0,index-1):
                temp=temp.next
            temp.next=temp.next.next
        self.size-=1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)