#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        dummy = Node("dummy")
        self.head = dummy
        self.tail = dummy

        self.current = None
        self.before = None

        self.num_of_data = 0

    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

        self.num_of_data += 1

    def delete(self):
        pop_data = self.current.data

        if self.current is self.tail:
            self.tail = self.before

        self.before.next = self.current.next
        self.current = self.before

        self.num_of_data -= 1

        return pop_data

    def first(self):
        if self.num_of_data == 0:
            return None

        self.before = self.head
        self.current = self.head.next

        return self.current.data

    def next(self):
        if self.current.next == None:
            return None

        self.before = self.current
        self.current = self.current.next

        return self.current.data

    def size(self):
        return self.num_of_data   


#!/usr/bin/env python
# coding: utf-8

# # traverse_all() 
# 
# ### head 부터 tail까지 값 출력
# #### 만약 데이터가 없으면 0을 출력하고, 아니라면 노드의 데이터를 data_list에 while 반복문으로 저장. 그리고 join함수로 리스트 내용 출력

# In[ ]:


def traverse_all(self):
    if self.num_of_data == 0:
        print("null")
        return
    else:
        data_list = []
        node = self.head.next
        while node:
            data_list.append(str(node.data))
            node = node.next
        print("->".join(["head"] + data_list + ["null"]))




# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




