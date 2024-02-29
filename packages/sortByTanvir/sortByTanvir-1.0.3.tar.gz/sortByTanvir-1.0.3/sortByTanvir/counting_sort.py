def counting_sort(array):
    if len(array) == 0:
        return array

    # Find the maximum value in the array
    max_val = max(array)
    size = len(array)

    # Initialize count array
    count = [0] * (max_val + 1)

    # Store the count of each element in the count array
    for num in array:
        count[num] += 1

    # Modify the count array to store the actual position of the element
    for i in range(1, max_val + 1):
        count[i] += count[i - 1]

    # Create the output array
    output = [0] * size

    # Build the output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into the original array
    for i in range(size):
        array[i] = output[i]

    return array
