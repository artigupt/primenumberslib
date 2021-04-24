def is_prime(n): 
  """ Fuction to check if a given number is a prime number.
  A prime number is defined as a number greter than 1 which is not a product of two strictly smaller numbers
  
  Args:
  n (int): integer to check
  
  Returns:
  bool: whether or not n is a prime number
  
  """
  
    i = 2
    flag = True
    while i < n:
        if n%i == 0:
            flag = False
            break
        i += 1
    return flag
    
