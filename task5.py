number = input("Enter a number: ")

digit_sum = 0

for digit in number:
    digit_sum += int(digit)

print("The sum of the digits is:", digit_sum)