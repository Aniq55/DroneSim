class survivor():
  ID= None
  x= None
  y= None
  marked_safe= None

  def __init__(self, ID, x, y):
      self.ID= ID
      self.x= x
      self.y= y
      self.marked_safe= False
