#test case 1 & 2 & 3
def add (y): 
  if y == " " or y =="0" :
    return 0
  else:
        x = y.split(',')
        num1 = int(x[0].strip())
        num2 = int(x[1].strip())
        c = num1 + num2
        return c
    
