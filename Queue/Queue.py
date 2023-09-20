class Queue:
  size = 0
  head = None
  tail = None
  def __init__(self):
    self.name = 'queue'

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
  
  def enqueue(self, value):
    if self.isEmpty():
      self.head = self.Node(value)
      self.head.next = None
      self.head.prev = None
      self.tail = self.head
      self.size += 1
    else:
      tail = self.Node(value)
      self.tail.next = tail
      tail.prev = self.tail
      self.tail = tail
      self.size += 1
  
  def dequeue(self):
    if self.isEmpty():
      return "queue is empty"
    
    next_head = self.head.next
    self.head.next = None
    next_head.prev = None
    self.head = None
    self.head = next_head
    self.size -= 1
  
  def peek(self):
    return self.head
  
  def contains(self, value):
    if self.isEmpty():
      return "queue is empty"
    
    i = 0
    check_value = self.head
    while i < self.size:
      if check_value.data == value:
        return check_value
      check_value = check_value.next
    
    return -1
  
  def remove(self, value):
    if self.isEmpty():
      return "queue is empty"
    
    i = 0
    check_node = self.head
    while i < self.size:
      if check_node.data == value:
        prev_node = check_node.prev
        next_node = check_node.next
        prev_node.next = None
        next_node.prev = None
        check_node.next = check_node.prev = None
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1
    
    return -1
    


