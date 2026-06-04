import collatz
def run():
    print("Enter a number")
    num=int(input())
    while num != 1:
        num = collatz.collatz(num)
run()