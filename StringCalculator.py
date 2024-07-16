#test case 1 & 2 & 3
def add(y):
    if y == " " or y == "0":
        return 0
    elif "," in y:
        x = y.split(',')
        if len(x) != 2:
            return "Invalid input: Please provide two numbers separated by a comma."
        
        try:
            num1 = int(x[0].strip())
            num2 = int(x[1].strip())
            result = num1 + num2
            return result
        except ValueError:
            return "Invalid input: Please provide valid integers separated by a comma."
    else:
        return "Invalid input: Please provide two numbers separated by a comma."
   

    
