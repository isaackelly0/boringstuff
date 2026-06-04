import collatz
def run():
    print("Enter a number:")
    try:
        num = int(input())
        while num != 1:
            num = collatz.collatz(num)
    except ValueError:
        print("Incorrect input, stick to integers")
run()