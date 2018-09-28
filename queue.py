class queue:
  def __init__(self):
    self.rear=None
    self.front=None
    self.value=[]

  def enqueue(self, x):
    self.value.append(x)
    if not self.rear and not self.front:
      print("Queue is empty")
      self.front=self.rear=0
    self.rear+=1   
    return True

  def dequeue(self):
    #print("deQueuing", self.rear, self.front,self.value[self.front])
    if self.value[self.front] is None:
       print('Queue is empty')
       return None
    temp= self.value[self.front]
    del self.value[self.front]
    if self.rear==0:
      self.rear=None
    self.rear-=1
    return temp

  def display(self):
    print("[ Front ->"),    
    for i in range(len(self.value)):
      print("{} ->".format(self.value[i])),
    print(" Rear]")    
    return True

  def length(self):
    return len(self.value)

if __name__ =="__main__":
  print("Started Queuing")
  q=queue()
  [ q.enqueue(i) for i in range(1,10)]
  q.display()
  print("Starting Dequeue operation")
  for i in range(q.length()):
    print(q.dequeue())
    q.display()
  





      