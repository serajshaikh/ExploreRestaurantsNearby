class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None

def create_linked_list():
    li=[int(ele) for ele in input().split()]
    head=None
    currNode=None
    for i in li:
        curr_node=Node(i)
        if head==None and currNode==None:
            head=curr_node
            currNode=head
        else:
            currNode.next=curr_node
            currNode=curr_node 
    return head
head=create_linked_list()
while head is not None:
    print(head.data, end=" ")
    head=head.next
