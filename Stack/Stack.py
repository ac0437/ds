class Stack:
  size = 0
  head = None
  tail = None
  def __init__(self):
    self.name = 'stack'

  class Node:
    data = None
    def __init__(self, data, prev, next):
      self.data = data
      self.prev = prev
      self.next = next

    def __repr__(self):
      return ''.join(self.data)
  
  def isEmpty(self):
    return self.size == 0
  
  def length(self):
    return self.size
  
  def push(self, node):
    if self.isEmpty():
      self.head = node
      self.head.next = None
      size += 1
      return node
    else:
      head = self.head
      head.prev = node
      self.head = node
      self.head.next = head
      return head
      
  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    
    head = self.head.next
    self.head.next = self.head.data = None
    self.head = head
    size -= 1

    return head
  
  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.head