# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 12:12:14 2018

@author: Deepesh K Rana
"""

class Node:
  def __init__(self):
    self.prev=None
    self.value=None
    self.next=None
    
class LL:
  def __init__(self):
    self.node= Node()
    self.head=self.node
  
  def append(self, x):
    print("insert",x)
    new=Node()
    new.value=x
    
    if self.head.value is None:
      self.head.prev=None
      self.head.value=x
      self.head.next=None
    else:
      current= self.head  
      while(current is not None):
        if current.next is None:
          current.next = new
          new.prev= current
          return True		  
        current = current.next

  def insertAt(self, x):
    print("insert",x)
    new=Node()
    new.value=x
    if self.head.value is None:
      self.head.prev=None
      self.head.value=x
      self.head.next=None
    else:
      current= self.head  
      while(current is not None):
        if current.value >= x:
          new.prev=current.prev
          new.next=current
          current.prev=new
		  #if current.next is None:
          return True 
        print(current.value)
        current = current.next
    return False	

  def remove(self):
    print("Remove")
    
  def search(self, x):
    current= self.head
    print("Starting Search "), 	
    while(current):
      print("->", current.value),
      current = current.next
  
  def display(self):
    current= self.head
    print("Head"), 	
    while(current):
      print("->", current.value),
      current = current.next
  

    
    
if __name__ =="__main__":
  ll=LL()
  for i in range(1,4):
    ll.append(i)
  for i in range(6,9):
    ll.append(i)
  ll.insertAt(5)
  ll.display()
    