#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print('[]')
    elif length == 1:
        print('[0]')
    else:
        # Initialize the sequence with the first two elements
        sequence = [0, 1]

        # Calculate the rest of the Fibonacci sequence
        for i in range(2, length):
            next_num = sequence[-1] + sequence[-2]
            sequence.append(next_num)

        # Print the Fibonacci sequence
        print(sequence)


# Run the function with the provided test cases
print_fibonacci(0)
print_fibonacci(1)
print_fibonacci(2)
print_fibonacci(10)
