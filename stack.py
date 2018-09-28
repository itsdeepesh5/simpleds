class stack: 
  def __init__(self, length):
    self.value=[]
    self.length=0
    if length:
      self.length=length
	  
  def push(self,x):
    if len(self.value) <= self.length:
	  if x:
	    self.value.append(x)
	    print('Pushed',x)
	  else:
	    print('Can not push anymore')	  
	
	
  def pop(self):
    #self.length    
	if self.value:
	  print('Popped')
  	  return self.value.pop()

	  
  def display(self):
    print("The Stack is {}".format(self.value))  
  
  def getlength(self):
    return self.length
  
if __name__ == "__main__":
  print("inside main")
  stk= stack(10)
  l = stk.getlength()
  print('Stack LEngth',l)
  [stk.push(i) for i in range(1,stk.getlength()+1)]
  print(stk.display())
  for i in range(stk.getlength()):
    print(stk.pop()) 
