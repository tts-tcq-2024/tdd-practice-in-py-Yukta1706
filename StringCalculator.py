#test case 1 & 2 & 3
def add(y):
    # Check for empty or whitespace-only input
    if not y.strip():
        return 0
    
    # Split input by comma and strip whitespace from components
    x = y.split(',')
    
    # Check if exactly two components were split
    if len(x) != 2:
        return "Invalid input: Please provide two numbers separated by a comma."
    
    # Try to convert components to integers and add them
    try:
        num1 = int(x[0].strip())
        num2 = int(x[1].strip())
        return num1 + num2
    except ValueError:
        return "Invalid input: Please provide valid integers separated by a comma."

    
