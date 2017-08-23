# The generator that produces the fibonacci sequence
def genfibon(n):
    a = 0 # Beginning seed of the sequence
    b = 1 # First number after the seed
    for i in range(n):
        yield a # The output from the generator. is the sum of the previous iteration + the current number
        a,b = b,a+b # Sets a to the next number in the sequence. Sets b to the sum of a+b prior to the reassignment.

# Actual program
def main():
    while True:
        input_numbers = int(raw_input('Please enter the quantity of Fibonacci numbers you would like to generate: '))
        for num in genfibon(input_numbers):
            print num

        continue_run = raw_input('Would you like to generate a different number?').lower()
        if continue_run <> 'y':
            break
        else:
            continue

# Call the actual program
main()
