class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    # invoke callback on current node
    cb(self.value)
    # apply callback to each node if self is not empty
    if self.left is not None:
      self.left.depth_first_for_each(cb)
    # same for right
    if self.right is not None:
      self.right.depth_first_for_each(cb)

  def breadth_first_for_each(self, cb):
    # queue data structure
    queue = [self]
    # iterate over search tree
    while len(queue) > 0:
      # apply cb to each tree element
      node = queue.pop(0)
      cb(node.value)
      # if a left node is found add it to the queue
      if node.left is not None:
        queue.append(node.left)
      # if right node is found add it to queue
      if node.right is not None:
        queue.append(node.right)

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
