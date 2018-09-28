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
      prev=self.head
      while(current is not None):
        print(current.value, new.value)
        if current.value >= x:
          prev.next=new
          new.next=current
          new.prev=current.prev
          current.prev=new
		  #if current.next is None:
          return True
        prev=current
        current = current.next
    return False

  def remove(self,x):
    current= self.head
    prev=self.head
    print("Starting Deletion "),
    while(current):
      if current.value == x:
        print("Found", current.value),
        prev.next=current.next
        current.next.prev =prev
        return True
      prev=current
      current = current.next
    print("Not Found", x),
    return False

  def search(self, x):
    current= self.head
    print("Starting Search "),
    indx=0
    while(current):
      if current.value == x:
        print("Found", current.value),
        return indx
      indx+=1
      current = current.next
    print("Not Found", x),
    return False

  def display(self):
    current= self.head
    print("Head"),
    while(current):
      print("->", current.value),
      current = current.next




if __name__ =="__main__":
  ll=LL()
  for i in range(1,10):
    ll.append(i)
  for i in range(30,36):
    ll.append(i)
  for i in range(11,29):
    ll.insertAt(i)
  ll.display()
  ll.search(12)
  ll.remove(10)
  ll.display()
