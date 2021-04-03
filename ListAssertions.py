class Asseritons:
  """
  Some functions, I was realised in order to check some common assertions
  """
  
  def check_int_float(self, list_: list) -> bool:
    """
    get list_ - [] 
    Check all elements are float or int
    O(n)
    return True or False
    """
    for i in list_:
      if type(i) != float or type(i) != int: 
        return False 
    return True 

  def check_assertion(self, vector_a: list, vector_b: list) -> None:
    """
    Check common vectors assertions
    """ 
    assert len(vector_a) > 0 and len(vector_b) > 0,  ('Vectors should have at least one argument')
    assert len(vector_a) == len(vector_b),  ('Vectors should be same size')
    assert (self.check_int_float(vector_a) == False or self.check_int_float(vector_b) == False),  ('Vectors should consist int or float values')
