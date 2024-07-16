def add(y):
    if not y.strip():  # Check for empty input
        return 0
    
    if y.startswith("//"):  # Check for custom delimiter
        delimiter_index = y.index("\n")
        delimiter = y[2:delimiter_index]
        numbers = y[delimiter_index+1:].split(delimiter)
    else:
        numbers = y.replace("\n", ",").split(",")

    # Convert numbers to integers and filter out numbers greater than 1000
    nums = [int(num) for num in numbers if num.isdigit() and int(num) <= 1000]

    # Check for invalid input with custom delimiter
    if any(not num.isdigit() for num in numbers if delimiter in num):
        return "Invalid input: Please provide valid integers separated by the custom delimiter."

    return sum(nums)
    
