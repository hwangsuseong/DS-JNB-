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

