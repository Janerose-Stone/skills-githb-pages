def generate_and_reverse(start_digit, end_digit):
    # Generate the list of numbers from start_digit to end_digit
    numbers = list(range(start_digit, end_digit + 1))

    # Reverse the list of numbers
    reversed_numbers = numbers[::-1]

    return reversed_numbers

# Input: Starting and ending digits
start_digit = int(input("Enter the starting digit: "))
end_digit = int(input("Enter the ending digit: "))

# Get the reversed list of numbers
reversed_numbers = generate_and_reverse(start_digit, end_digit)

# Output: Display the reversed list of numbers
print("Reversed numbers between {} and {}:".format(start_digit, end_digit))
print(reversed_numbers)


