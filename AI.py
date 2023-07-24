def fibonacci_sequence(n):
    if n <= 0:
        return []

    fibonacci_numbers = [0, 1]

    for i in range(2, n):
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_number)

    return fibonacci_numbers

# Get the user input for the number of Fibonacci numbers to generate
try:
    num_terms = int(input("Enter the number of Fibonacci numbers to generate: "))
    if num_terms < 0:
        raise ValueError("Number of terms should be a non-negative integer.")
except ValueError as e:
    print("Invalid input. Please enter a non-negative integer.")
else:
    fibonacci_sequence = fibonacci_sequence(num_terms)
    print("Fibonacci sequence:")
    print(fibonacci_sequence)
9
